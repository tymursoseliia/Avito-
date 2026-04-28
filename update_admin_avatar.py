import re

html_file = 'admin.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add file input for author avatar
html = html.replace('''<div class="form-group">
                        <label>Имя автора</label>
                        <input type="text" id="review_author" required>
                    </div>''', 
                    '''<div class="form-group">
                        <label>Имя автора</label>
                        <input type="text" id="review_author" required>
                    </div>
                    <div class="form-group">
                        <label>Аватар автора (необязательно)</label>
                        <input type="file" id="author_avatar" accept="image/*">
                        <div id="author-avatar-name" style="font-size: 13px; color: #666; margin-top: 4px;"></div>
                    </div>''')

# 2. Add event listener to show file name
js_addition = '''
        document.getElementById('author_avatar').addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                document.getElementById('author-avatar-name').textContent = '📷 ' + e.target.files[0].name;
            } else {
                document.getElementById('author-avatar-name').textContent = '';
            }
        });
'''
if 'author-avatar-name' not in html: # Prevent double inject
    html = html.replace('''document.getElementById('review_images').addEventListener''', js_addition + '''\n        document.getElementById('review_images').addEventListener''')

# 3. Update startReviewEdit to reset author avatar field
html = html.replace('''document.getElementById('review_author').value = r.author_name || '';''', 
                    '''document.getElementById('review_author').value = r.author_name || '';
            document.getElementById('author_avatar').value = '';
            document.getElementById('author-avatar-name').textContent = r.author_avatar ? '📷 Установлен текущий аватар' : '';''')

# 4. Update cancelReviewEdit to reset author avatar field
html = html.replace('''document.getElementById('review_author').value = '';''',
                    '''document.getElementById('review_author').value = '';
            document.getElementById('author_avatar').value = '';
            document.getElementById('author-avatar-name').textContent = '';''')

# 5. Update review submit logic to upload author avatar
# Find `const author = document.getElementById('review_author').value;`
# and `let comment_photos = []; let reply_photos = [];`
# Add `let author_avatar_url = null;`
submit_logic_start = html.find('''const author = document.getElementById('review_author').value;''')
if submit_logic_start != -1:
    html = html.replace('''let comment_photos = [];''', '''let comment_photos = [];
                let reply_photos = [];
                let author_avatar_url = null;
                
                // Upload author avatar if selected
                const avatarFile = document.getElementById('author_avatar').files[0];
                if (avatarFile) {
                    const ext = avatarFile.name.split('.').pop();
                    const path = `reviews/${Date.now()}_avatar.${ext}`;
                    const { data, error } = await supabaseClient.storage.from('cars').upload(path, avatarFile);
                    if (error) throw new Error('Ошибка загрузки аватара автора');
                    author_avatar_url = supabaseClient.storage.from('cars').getPublicUrl(path).data.publicUrl;
                } else if (editId) {
                    const existingReview = allReviews.find(r => r.id === editId);
                    if (existingReview) author_avatar_url = existingReview.author_avatar;
                }
                
                // This comment_photos = [] is to avoid duplicate declarations since I replaced it''')

    # Now modify the actual insert/update object
    html = html.replace('''author_name: author,''', '''author_name: author,\n                            author_avatar: author_avatar_url,''')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated admin.html for author avatar.")
