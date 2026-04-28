import re

with open('original_review.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Replace variables in `orig` to make it a JS template string.
# We will use this in `clean_avito (1).html`
template = orig

# Replace Author
template = re.sub(r'<h5([^>]*)>Владимир</h5>', r'<h5\1>${r.author_name}</h5>', template)

# Replace Date
template = re.sub(r'<p([^>]*)>28 марта</p>', r'<p\1>${r.date_text}</p>', template)

# Replace Rating Meta
template = re.sub(r'<meta itemprop="ratingValue" content="5">', r'<meta itemprop="ratingValue" content="${r.rating}">', template)

# Replace Car Title
template = re.sub(r'<span itemprop="name"([^>]*)>Audi Q5 2\.0 AMT, 2025, 11&nbsp;км</span>', r'<span itemprop="name"\1>${r.car_title}</span>', template)

# Replace Comment Text
# <p class="..." data-marker="review(1)/text-section/text">Хороший салон... покупаем.</p>
# It spans multiple lines, so we use regex with DOTALL
template = re.sub(r'(<p[^>]*data-marker="review\(1\)/text-section/text">)[\s\S]*?(</p>)', r'\1${r.comment_text}\2', template)

# Replace Reply Text
# <p class="..." data-marker="review(1)/text-section/text">Уважаемый... со всего Мира</p>
# Wait, the reply text also has data-marker="review(1)/text-section/text"? No, let's see.
# Ah, the reply text is inside `<div class="styles-module-answer-UU7zu">... <p class="..." data-marker="review(1)/text-section/text">`
# Let's replace the whole reply section dynamically if there is a reply.
# Find where the reply block starts: <div data-marker="review(1)/answer"
reply_idx = template.find('<div data-marker="review(1)/answer"')
if reply_idx != -1:
    comment_part = template[:reply_idx]
    reply_part_orig = template[reply_idx:]
    
    # In reply_part, replace the text
    reply_part = re.sub(r'(<p[^>]*data-marker="review\(1\)/text-section/text">)[\s\S]*?(</p>)', r'\1${r.reply_text}\2', reply_part_orig)
    
    # Wait, the reply might have its own date and author name (Автомиг)
    reply_part = re.sub(r'<p([^>]*)>6 апреля</p>', r'<p\1>Официальный ответ</p>', reply_part)
    
    # Make reply optional
    reply_template = "${r.reply_text ? `" + reply_part.replace('`', '\\`') + "` : ''}"
    template = comment_part + reply_template
else:
    # If no reply part found, just leave it
    pass

# We also need to replace the data-marker="review(1)" with review(${index+1})
template = template.replace('review(1)', 'review(${index+1})')

# We need to replace the stars generation
# Original has 5 stars, we need to generate them dynamically.
# Let's find `<div class="styles-module-root-Tqjuo">...</div>` that contains `data-marker="review(1)/score"`
# Actually, we can just replace the innerHTML of `styles-module-root-Tqjuo` with `${starsHtml}`
# It looks like:
# <div data-marker="review(1)/score" ... class="styles-module-root-Tqjuo"><meta ...> ... <div ...star-1... </div> ... <div ...star-5... </div></div>
# We can use regex to replace all the `star-X` divs
template = re.sub(r'(<meta itemprop="ratingValue" content="\$\{r\.rating\}">).*?(</div>\s*</div>\s*<p itemprop="itemReviewed")', r'\1\n${starsHtml}\n\2', template, flags=re.DOTALL)

# Handle Comment Photos
# The original review has `<div class="styles-module-component-after-Y15nP"></div></header><div data-marker="review(${index+1})/body">`
# The images are inside `styles-module-images-ycitL`
# Let's completely replace the images section with `${commentPhotosHtml}` if they exist.
# Find `<div class="styles-module-images-ycitL">` and replace up to its matching `</div></div></div></div>`
# Wait, it's safer to just let JS build it.
# Actually, the original review didn't have comment photos! The reply had photos!
# "Фото из отзыва" - wait, did the comment or reply have photos?
# `original_review.html` had photos inside the reply or the comment?
# Let's look at `reply_part_orig`. The images are BEFORE `styles-module-textSection-ivuRS` inside the reply block!
# Let's just output the python template so I can manually verify it.
with open('js_template.js', 'w', encoding='utf-8') as f:
    f.write(template)
print("Template created in js_template.js")
