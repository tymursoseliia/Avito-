with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Variable declarations
html = html.replace(
    "const carsListEl = document.getElementById('cars-list');",
    "const carsListEl = document.getElementById('cars-list');\n        const reviewsListEl = document.getElementById('reviews-list');"
)
html = html.replace("const reviewsListEl = document.getElementById('reviews-list');", "", 1) # remove the second one later

# Fix 2: Remove early calls
html = html.replace("loadAdminCars();\n        loadAdminReviews();\n\n        \n        \n        }", "}")

# Fix 3: Image removal UI logic
# Replace the file lists rendering in startReviewEdit
old_review_edit = """            let reviewFilesHtml = '';
            if (r.comment_photos && r.comment_photos.length > 0) {
                reviewFilesHtml = r.comment_photos.map(url => `<div>📷 <a href="${url}" target="_blank" style="color:#00AAFF;">Уже загруженное фото</a></div>`).join('');
            }
            document.getElementById('review-file-list').innerHTML = reviewFilesHtml;

            let replyFilesHtml = '';
            if (r.reply_photos && r.reply_photos.length > 0) {
                replyFilesHtml = r.reply_photos.map(url => `<div>📷 <a href="${url}" target="_blank" style="color:#00AAFF;">Уже загруженное фото</a></div>`).join('');
            }
            document.getElementById('reply-file-list').innerHTML = replyFilesHtml;"""

new_review_edit = """            currentReviewPhotos = r.comment_photos ? [...r.comment_photos] : [];
            currentReplyPhotos = r.reply_photos ? [...r.reply_photos] : [];
            renderExistingReviewPhotos();
            renderExistingReplyPhotos();"""

html = html.replace(old_review_edit, new_review_edit)

# Add globals
html = html.replace("let selectedReviewFiles = [];", "let selectedReviewFiles = [];\n        let currentReviewPhotos = [];\n        let currentReplyPhotos = [];\n")

# Add render functions
render_functions = """
        function renderExistingReviewPhotos() {
            const list = document.getElementById('review-file-list');
            let html = currentReviewPhotos.map((url, i) => `
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <img src="${url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; margin-right: 12px;">
                    <span onclick="removeExistingReviewPhoto(${i})" style="color:red; cursor:pointer; font-size: 14px;">❌ Удалить</span>
                </div>
            `).join('');
            
            let newFilesHtml = selectedReviewFiles.map(f => `<div>📷 Новый файл: ${f.name}</div>`).join('');
            list.innerHTML = html + newFilesHtml;
        }

        function removeExistingReviewPhoto(index) {
            currentReviewPhotos.splice(index, 1);
            renderExistingReviewPhotos();
        }

        function renderExistingReplyPhotos() {
            const list = document.getElementById('reply-file-list');
            let html = currentReplyPhotos.map((url, i) => `
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <img src="${url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; margin-right: 12px;">
                    <span onclick="removeExistingReplyPhoto(${i})" style="color:red; cursor:pointer; font-size: 14px;">❌ Удалить</span>
                </div>
            `).join('');
            
            let newFilesHtml = selectedReplyFiles.map(f => `<div>📷 Новый файл: ${f.name}</div>`).join('');
            list.innerHTML = html + newFilesHtml;
        }

        function removeExistingReplyPhoto(index) {
            currentReplyPhotos.splice(index, 1);
            renderExistingReplyPhotos();
        }
"""
html = html.replace("function startReviewEdit(id) {", render_functions + "\n        function startReviewEdit(id) {")

# Update file change listeners
html = html.replace(
    "list.innerHTML = selectedReviewFiles.map(f => `<div>📷 ${f.name}</div>`).join('');",
    "renderExistingReviewPhotos();"
)
html = html.replace(
    "list.innerHTML = selectedReplyFiles.map(f => `<div>📷 ${f.name}</div>`).join('');",
    "renderExistingReplyPhotos();"
)

# Update submit logic
old_submit_start = """                let reviewPhotoUrls = [];
                let replyPhotoUrls = [];
                let author_avatar_url = null;"""
new_submit_start = """                let reviewPhotoUrls = [...currentReviewPhotos];
                let replyPhotoUrls = [...currentReplyPhotos];
                let author_avatar_url = null;"""
html = html.replace(old_submit_start, new_submit_start)

old_submit_end = """                if (reviewPhotoUrls.length > 0) revData.comment_photos = reviewPhotoUrls;
                if (replyPhotoUrls.length > 0) revData.reply_photos = replyPhotoUrls;"""
new_submit_end = """                revData.comment_photos = reviewPhotoUrls;
                revData.reply_photos = replyPhotoUrls;"""
html = html.replace(old_submit_end, new_submit_end)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
