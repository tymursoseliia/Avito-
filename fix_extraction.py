import re
import json

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

review_blocks = re.split(r'data-marker="review\(\d+\)"', html)[1:]
reviews_data = []

for block in review_blocks:
    # Check if this block is actually a review (some splits might be nested answer markers)
    if 'class="styles-module-root-eNKJJ"' not in block:
        continue

    # Author
    author_match = re.search(r'<h5[^>]*>([^<]+)</h5>', block)
    author_name = author_match.group(1).strip() if author_match else "Неизвестный"
    
    # Date Text
    header_end = block.find('</header>')
    if header_end != -1:
        date_match = re.search(r'<p[^>]*>([^<]+)</p>', block[:header_end])
        date_text = date_match.group(1).strip() if date_match else "Недавно"
    else:
        date_text = "Недавно"
        
    # Car Title
    car_match = re.search(r'itemTitle"[^>]*>(.*?)</span>', block)
    if car_match:
        car_title = re.sub(r'<[^>]+>', '', car_match.group(1)).strip().replace('&nbsp;', ' ')
    else:
        car_title = "Автомобиль"

    # Rating
    rating_match = re.search(r'itemprop="ratingValue" content="(\d+)"', block)
    rating = int(rating_match.group(1)) if rating_match else 5

    # Comment text and Reply text
    # Both use `data-marker="review(...)/text-section/text"`
    # But reply is inside `class="styles-module-answer`
    answer_idx = block.find('class="styles-module-answer-')
    
    if answer_idx != -1:
        comment_part = block[:answer_idx]
        reply_part = block[answer_idx:]
    else:
        comment_part = block
        reply_part = ""

    comment_match = re.search(r'text-section/text"[^>]*>([\s\S]*?)</p>', comment_part)
    comment_text = comment_match.group(1).strip() if comment_match else ""
    
    reply_match = re.search(r'text-section/text"[^>]*>([\s\S]*?)</p>', reply_part)
    reply_text = reply_match.group(1).strip() if reply_match else ""
    
    # Strip HTML tags
    comment_text = re.sub(r'<br/?>', '\n', comment_text)
    comment_text = re.sub(r'<[^>]+>', '', comment_text).strip()
    
    reply_text = re.sub(r'<br/?>', '\n', reply_text)
    reply_text = re.sub(r'<[^>]+>', '', reply_text).strip()

    if comment_text:
        reviews_data.append({
            "author_name": author_name,
            "rating": rating,
            "date_text": date_text,
            "car_title": car_title,
            "comment_text": comment_text,
            "reply_text": reply_text
        })

with open('extracted_reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(reviews_data)} reviews. Replies found: {sum(1 for r in reviews_data if r['reply_text'])}")
