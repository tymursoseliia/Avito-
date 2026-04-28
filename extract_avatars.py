import re
import json

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

avatars = []
for m in re.finditer(r'data-marker="avatar"[^>]*>', html):
    start = m.start()
    end = html.find('</div>', start)
    if end == -1: end = start + 200
    avatars.append(html[start:end])

# Also find data-marker="review/avatar" or something
for m in re.finditer(r'avatar', html):
    start = max(0, m.start() - 50)
    end = min(len(html), m.start() + 150)
    if 'data-marker' in html[start:end]:
        # print(html[start:end])
        pass

with open('all_avatars.json', 'w', encoding='utf-8') as f:
    json.dump(avatars, f, ensure_ascii=False, indent=2)

print(f"Found {len(avatars)} avatar markers")
