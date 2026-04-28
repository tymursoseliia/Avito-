import sys
import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

text = 'Каталог автомобилей'
url = 'https://www.avito.ru/catalog/auto-ASgBAgICAUTQvA7~m9EB'

idx = html.find(text)
if idx != -1:
    a_start = html.rfind('<a ', 0, idx)
    a_end = html.find('>', a_start) + 1
    
    a_tag = html[a_start:a_end]
    print(f"Original a_tag: {a_tag}")
    
    if 'href=' in a_tag:
        new_a_tag = re.sub(r'href="[^"]+"', f'href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;"', a_tag)
    else:
        new_a_tag = a_tag.replace('<a ', f'<a href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;" ')
    
    print(f"New a_tag: {new_a_tag}")
    html = html[:a_start] + new_a_tag + html[a_end:]

    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Link updated.")
else:
    print("Text not found.")
