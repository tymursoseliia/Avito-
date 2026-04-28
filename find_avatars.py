import json
import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

matches = []
# Find all avatar containers
for m in re.finditer(r'data-marker="avatar"', html):
    idx = m.start()
    matches.append(html[max(0, idx-100):idx+300])

with open('find_avatars.json', 'w', encoding='utf-8') as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

print(f"Found {len(matches)} avatars")
