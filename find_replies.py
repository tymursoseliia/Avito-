import json
import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

matches = []
for m in re.finditer(r'Ответ продавца', html):
    idx = m.start()
    matches.append(html[max(0, idx-400):idx+400])

with open('find_replies.json', 'w', encoding='utf-8') as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

print(f"Found {len(matches)} seller replies")
