import re
import json
import urllib.request

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all review blocks
# Each review starts with <div data-marker="review(N)"
review_blocks = re.split(r'data-marker="review\(\d+\)"', html)[1:] # Skip the part before the first review

reviews_data = []

for block in review_blocks:
    # Author Name
    # <h5 ...>Author Name</h5>
    author_match = re.search(r'<h5[^>]*>([^<]+)</h5>', block)
    author_name = author_match.group(1).strip() if author_match else "Неизвестный"
    
    # Date Text
    # <p class="... stylesMarningNormal-module-paragraph-s-dense-H7b3C">Date Text</p>
    # The date is usually the first <p> after the author name in the header.
    # Let's find the header block
    header_end = block.find('</header>')
    if header_end != -1:
        date_match = re.search(r'<p[^>]*>([^<]+)</p>', block[:header_end])
        date_text = date_match.group(1).strip() if date_match else ""
    else:
        date_text = ""
        
    # If date_text is missing or looks like "171 отзывов", we might need a better regex.
    # Actually, Avito date text is like "2 недели назад"
    
    # Car Title
    # data-marker="review(N)/itemTitle">Car Title...</span></p> or something
    # Let's just search for itemTitle
    car_match = re.search(r'itemTitle"[^>]*>(.*?)</span>', block)
    if car_match:
        car_title = re.sub(r'<[^>]+>', '', car_match.group(1)).strip()
        car_title = car_title.replace('&nbsp;', ' ')
    else:
        car_title = "Автомобиль"

    # Comment text
    # data-marker="review(N)/text-section/text">Comment text</p>
    comment_match = re.search(r'text-section/text"[^>]*>([\s\S]*?)</p>', block)
    if comment_match:
        comment_text = comment_match.group(1).strip()
    else:
        comment_text = ""
        
    # Reply text
    # The reply block usually has an <h5>Автосалон Автомиг...</h5> and then a <p> with the text
    # Or class styles-module-answer-UU7zu
    reply_match = re.search(r'class="styles-module-answer[^>]+>([\s\S]*?)</div></div></div>', block)
    reply_text = ""
    if reply_match:
        reply_html = reply_match.group(1)
        # Find the <p> tag inside reply_html
        p_match = re.search(r'<p[^>]*>([\s\S]*?)</p>', reply_html)
        if p_match:
            reply_text = p_match.group(1).strip()
            
    # Rating
    # Count how many filled stars
    # <div data-marker="review(N)/ratingStars/star-1"
    # We can just count how many styles-module-filled
    # Actually it's easier to find the meta itemprop="ratingValue" content="5"
    rating_match = re.search(r'itemprop="ratingValue" content="(\d+)"', block)
    rating = int(rating_match.group(1)) if rating_match else 5
    
    # Clean up texts
    comment_text = comment_text.replace('\n', ' ').strip()
    reply_text = reply_text.replace('\n', ' ').strip()
    
    if comment_text:
        reviews_data.append({
            "author_name": author_name,
            "rating": rating,
            "date_text": date_text,
            "car_title": car_title,
            "comment_text": comment_text,
            "reply_text": reply_text
        })

# Print found reviews
with open('extracted_reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(reviews_data)} reviews")
