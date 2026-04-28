with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r"getElementById\('([^']+)'\)", html)
for match in set(matches):
    if f'id="{match}"' not in html:
        print('MISSING ID:', match)
