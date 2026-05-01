import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see context around Автомиг to make sure we don't break URLs
for match in re.finditer(r'.{0,30}Автомиг.{0,30}', html, re.IGNORECASE):
    print(match.group(0).encode('utf-8'))
