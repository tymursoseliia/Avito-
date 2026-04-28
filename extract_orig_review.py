import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# We know reviews are inside `styles-module-snippet-JUn6v`
matches = list(re.finditer(r'<div class="styles-module-snippet-JUn6v">', html))

# Find the one that contains `data-marker="review(1)"`
for i, m in enumerate(matches):
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(html)
    snippet = html[start:end]
    if 'data-marker="review(1)"' in snippet:
        with open('original_review.html', 'w', encoding='utf-8') as out:
            out.write(snippet)
        print("Saved to original_review.html")
        break
