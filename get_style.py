import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'id="custom-auto-filters"[^>]*style="([^"]*)"', html)
if match:
    print(f"STYLE: {match.group(1)}")
else:
    print("Not found")
