import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

script = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script:
    script = script.group(1)
    ids = re.findall(r"document\.getElementById\('([^']+)'\)", script)
    
    missing = []
    for id_val in set(ids):
        if f'id="{id_val}"' not in html:
            missing.append(id_val)
            
    print('Missing IDs in DOM:')
    for m in missing:
        print(m)
