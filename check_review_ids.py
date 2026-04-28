with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('edit_review_id exists:', 'id="edit_review_id"' in html)
print('review_author exists:', 'id="review_author"' in html)
print('author_avatar exists:', 'id="author_avatar"' in html)
print('review_rating exists:', 'id="review_rating"' in html)
print('review_date exists:', 'id="review_date"' in html)
print('review_car_title exists:', 'id="review_car_title"' in html)
print('review_comment exists:', 'id="review_comment"' in html)
print('review_reply exists:', 'id="review_reply"' in html)
