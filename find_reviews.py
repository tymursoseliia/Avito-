import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

matches = []
for m in re.finditer(r'Отзывы', html):
    idx = m.start()
    matches.append(html[max(0, idx-100):idx+300])

with open('find_reviews.txt', 'w', encoding='utf-8') as f:
    for i, m in enumerate(matches):
        f.write(f"--- MATCH {i} ---\n{m}\n\n")

print(f"Found {len(matches)} matches")
