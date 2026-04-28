with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()
print('add-review-form exists:', 'id="add-review-form"' in html)
print('review-submit-btn exists:', 'id="review-submit-btn"' in html)
print('review_images exists:', 'id="review_images"' in html)
print('reply_images exists:', 'id="reply_images"' in html)
print('review-form-title exists:', 'id="review-form-title"' in html)
