import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for tabs
if '.tabs {' not in html:
    css_tabs = '''
        .tabs {
            display: flex;
            gap: 24px;
            margin: 0 auto 24px;
            max-width: 1200px;
            padding: 0 24px;
            border-bottom: 1px solid #e0e0e0;
        }
        .tab {
            cursor: pointer;
            padding: 12px 0;
            font-weight: 600;
            font-size: 16px;
            border-bottom: 3px solid transparent;
            color: #666;
            margin-right: 24px;
        }
        .tab.active {
            color: #00AAFF;
            border-bottom-color: #00AAFF;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        /* Make sure file uploads can scroll if too many */
        #review-file-list, #reply-file-list {
            margin-top: 12px;
            font-size: 14px;
            color: #333;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
'''
    html = html.replace('</style>', css_tabs + '</style>')

# Inject Tabs HTML before main-layout
if '<div class="tabs">' not in html:
    tabs_html = '''
    <div class="tabs">
        <div class="tab active" onclick="switchTab('cars', this)">🚘 Автомобили</div>
        <div class="tab" onclick="switchTab('reviews', this)">💬 Отзывы</div>
    </div>
    
    <div id="cars-tab" class="tab-content active">
'''
    html = html.replace('<div class="main-layout">', tabs_html + '<div class="main-layout">')

# Add Reviews Tab HTML after the first main-layout
if '<div id="reviews-tab"' not in html:
    reviews_html = '''
    </div> <!-- Close cars-tab -->
    
    <div id="reviews-tab" class="tab-content">
        <div class="main-layout">
            <!-- Форма отзывов -->
            <div class="container">
                <h1 id="review-form-title">
                    Новый отзыв
                    <span class="cancel-edit-btn" id="review-cancel-edit-btn" onclick="cancelReviewEdit()">Отменить</span>
                </h1>
                <form id="add-review-form">
                    <input type="hidden" id="edit_review_id">
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label class="form-label" for="review_author">Имя автора</label>
                            <input type="text" id="review_author" class="form-input" placeholder="Например: Иван" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="review_rating">Оценка (звезды)</label>
                            <select id="review_rating" class="form-input" required>
                                <option value="5">5 звезд</option>
                                <option value="4">4 звезды</option>
                                <option value="3">3 звезды</option>
                                <option value="2">2 звезды</option>
                                <option value="1">1 звезда</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label class="form-label" for="review_date">Дата отзыва</label>
                            <input type="text" id="review_date" class="form-input" placeholder="Например: 2 недели назад" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="review_car_title">Название авто</label>
                            <input type="text" id="review_car_title" class="form-input" placeholder="Audi Q5..." required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label" for="review_comment">Текст комментария клиента</label>
                        <textarea id="review_comment" class="form-input" rows="4" placeholder="Текст отзыва..." required></textarea>
                    </div>

                    <div class="form-group">
                        <label class="form-label" id="review-photo-label">Фото клиента (к отзыву)</label>
                        <div class="file-upload-wrapper">
                            <div class="file-upload-text">+ Выбрать фото</div>
                            <input type="file" id="review_images" accept="image/*" multiple>
                        </div>
                        <div id="review-file-list"></div>
                    </div>
                    
                    <hr style="margin: 32px 0; border: none; border-top: 1px solid #ddd;">
                    <h2 style="font-size: 18px; margin-bottom: 16px;">Ваш ответ</h2>

                    <div class="form-group">
                        <label class="form-label" for="review_reply">Текст ответа</label>
                        <textarea id="review_reply" class="form-input" rows="4" placeholder="С теплыми пожеланиями, Автосалон Автомиг..."></textarea>
                    </div>

                    <div class="form-group">
                        <label class="form-label" id="reply-photo-label">Фото автосалона (к ответу)</label>
                        <div class="file-upload-wrapper" style="background-color: #f6ffed; border-color: #52c41a;">
                            <div class="file-upload-text" style="color: #52c41a;">+ Выбрать фото ответа</div>
                            <input type="file" id="reply_images" accept="image/*" multiple>
                        </div>
                        <div id="reply-file-list"></div>
                    </div>

                    <button type="submit" class="submit-btn" id="review-submit-btn">Опубликовать отзыв</button>
                </form>
            </div>

            <!-- Список отзывов -->
            <div class="list-container">
                <h1>Существующие отзывы</h1>
                <div id="reviews-list">
                    Загрузка...
                </div>
            </div>
        </div>
    </div>
'''
    # We find the closing div of cars-tab.
    # Currently the structure is:
    # <div class="main-layout"> ... </div>
    # <div id="toast" class="toast">Автомобиль успешно добавлен!</div>
    # We will replace <div id="toast" with `reviews_html + <div id="toast"`
    html = html.replace('<div id="toast"', reviews_html + '\n    <div id="toast"')


# Now add JS for Reviews
if 'function switchTab(' not in html:
    js_code = '''
        function switchTab(tabId, el) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(tabId + '-tab').classList.add('active');
            el.classList.add('active');
        }

        const reviewForm = document.getElementById('add-review-form');
        const reviewSubmitBtn = document.getElementById('review-submit-btn');
        const reviewsListEl = document.getElementById('reviews-list');
        
        let selectedReviewFiles = [];
        let selectedReplyFiles = [];
        let allReviews = [];

        document.getElementById('review_images').addEventListener('change', (e) => {
            selectedReviewFiles = Array.from(e.target.files).slice(0, 5);
            const list = document.getElementById('review-file-list');
            list.innerHTML = selectedReviewFiles.map(f => `<div>📷 ${f.name}</div>`).join('');
        });

        document.getElementById('reply_images').addEventListener('change', (e) => {
            selectedReplyFiles = Array.from(e.target.files).slice(0, 5);
            const list = document.getElementById('reply-file-list');
            list.innerHTML = selectedReplyFiles.map(f => `<div>📷 ${f.name}</div>`).join('');
        });

        async function loadAdminReviews() {
            const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
            if (error) {
                reviewsListEl.innerHTML = '<span style="color:red">Ошибка загрузки отзывов</span>';
                return;
            }
            allReviews = data || [];
            renderReviews();
        }

        function renderReviews() {
            if (allReviews.length === 0) {
                reviewsListEl.innerHTML = '<p>Пока нет отзывов.</p>';
                return;
            }
            reviewsListEl.innerHTML = allReviews.map(r => `
                <div class="car-item">
                    <div class="car-item-info">
                        <div class="car-item-title">${r.author_name} - ${r.rating} ⭐</div>
                        <div style="font-size: 13px; color: #666;">${r.date_text} • ${r.car_title}</div>
                        <div style="margin-top: 8px; font-size: 14px;">${r.comment_text.substring(0, 100)}...</div>
                        ${r.reply_text ? `<div style="margin-top: 4px; font-size: 13px; color: #00AAFF;">Ответ: ${r.reply_text.substring(0, 50)}...</div>` : ''}
                    </div>
                    <div class="car-item-actions">
                        <button class="action-btn edit" onclick="startReviewEdit('${r.id}')">Редактировать</button>
                        <button class="action-btn delete" onclick="deleteReview('${r.id}')">Удалить</button>
                    </div>
                </div>
            `).join('');
        }

        async function deleteReview(id) {
            if(!confirm('Вы уверены, что хотите удалить этот отзыв?')) return;
            const { error } = await supabaseClient.from('reviews').delete().eq('id', id);
            if (error) {
                showToast('Ошибка удаления', true);
            } else {
                showToast('Отзыв удален!');
                loadAdminReviews();
                if(document.getElementById('edit_review_id').value === id) cancelReviewEdit();
            }
        }

        function startReviewEdit(id) {
            const r = allReviews.find(x => x.id === id);
            if(!r) return;

            document.getElementById('edit_review_id').value = r.id;
            document.getElementById('review_author').value = r.author_name || '';
            document.getElementById('review_rating').value = r.rating || '5';
            document.getElementById('review_date').value = r.date_text || '';
            document.getElementById('review_car_title').value = r.car_title || '';
            document.getElementById('review_comment').value = r.comment_text || '';
            document.getElementById('review_reply').value = r.reply_text || '';
            
            document.getElementById('review-form-title').childNodes[0].nodeValue = 'Редактирование отзыва ';
            document.getElementById('review-cancel-edit-btn').style.display = 'block';
            reviewSubmitBtn.textContent = 'Сохранить изменения';
            
            selectedReviewFiles = [];
            selectedReplyFiles = [];
            document.getElementById('review-file-list').innerHTML = '';
            document.getElementById('reply-file-list').innerHTML = '';
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function cancelReviewEdit() {
            reviewForm.reset();
            document.getElementById('edit_review_id').value = '';
            document.getElementById('review-form-title').childNodes[0].nodeValue = 'Новый отзыв ';
            document.getElementById('review-cancel-edit-btn').style.display = 'none';
            reviewSubmitBtn.textContent = 'Опубликовать отзыв';
            selectedReviewFiles = [];
            selectedReplyFiles = [];
            document.getElementById('review-file-list').innerHTML = '';
            document.getElementById('reply-file-list').innerHTML = '';
        }

        reviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const editId = document.getElementById('edit_review_id').value;
            
            reviewSubmitBtn.disabled = true;
            reviewSubmitBtn.textContent = 'Обработка...';

            try {
                let reviewPhotoUrls = [];
                let replyPhotoUrls = [];

                // Upload Review Photos
                if (selectedReviewFiles.length > 0) {
                    for (let i = 0; i < selectedReviewFiles.length; i++) {
                        reviewSubmitBtn.textContent = `Загрузка фото клиента ${i + 1}...`;
                        const fileName = `reviews/${Date.now()}_rev_${Math.random().toString(36).substring(7)}.jpg`;
                        const { error: uploadError } = await supabaseClient.storage.from('cars').upload(fileName, selectedReviewFiles[i]);
                        if (!uploadError) {
                            const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                            reviewPhotoUrls.push(publicUrl);
                        }
                    }
                }

                // Upload Reply Photos
                if (selectedReplyFiles.length > 0) {
                    for (let i = 0; i < selectedReplyFiles.length; i++) {
                        reviewSubmitBtn.textContent = `Загрузка фото ответа ${i + 1}...`;
                        const fileName = `reviews/${Date.now()}_rep_${Math.random().toString(36).substring(7)}.jpg`;
                        const { error: uploadError } = await supabaseClient.storage.from('cars').upload(fileName, selectedReplyFiles[i]);
                        if (!uploadError) {
                            const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                            replyPhotoUrls.push(publicUrl);
                        }
                    }
                }

                reviewSubmitBtn.textContent = 'Сохранение отзыва...';

                const revData = {
                    author_name: document.getElementById('review_author').value.trim(),
                    rating: parseInt(document.getElementById('review_rating').value),
                    date_text: document.getElementById('review_date').value.trim(),
                    car_title: document.getElementById('review_car_title').value.trim(),
                    comment_text: document.getElementById('review_comment').value.trim(),
                    reply_text: document.getElementById('review_reply').value.trim()
                };

                if (reviewPhotoUrls.length > 0) revData.comment_photos = reviewPhotoUrls;
                if (replyPhotoUrls.length > 0) revData.reply_photos = replyPhotoUrls;

                let error = null;
                
                if (editId) {
                    const res = await supabaseClient.from('reviews').update(revData).eq('id', editId);
                    error = res.error;
                } else {
                    const res = await supabaseClient.from('reviews').insert([revData]);
                    error = res.error;
                }

                if (error) throw new Error('Ошибка БД: ' + error.message);

                showToast(editId ? 'Отзыв изменен!' : 'Отзыв добавлен!');
                cancelReviewEdit();
                loadAdminReviews();
            } catch (err) {
                console.error(err);
                showToast(err.message, true);
            } finally {
                reviewSubmitBtn.disabled = false;
                reviewSubmitBtn.textContent = editId ? 'Сохранить изменения' : 'Опубликовать отзыв';
            }
        });
        
        loadAdminReviews();
'''
    html = html.replace('// Запуск\n        loadAdminCars();', '// Запуск\n        loadAdminCars();\n' + js_code)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated admin.html with Reviews tab!")
