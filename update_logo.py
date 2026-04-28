import sys
import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# The main logo is usually the first link with href="/" in the header
# Or we can search for the aria-label="Авито" or title="Авито"
idx = html.find('href="/"')
if idx != -1:
    a_start = html.rfind('<a ', 0, idx)
    a_end = html.find('>', a_start) + 1
    
    a_tag = html[a_start:a_end]
    print(f"Original a_tag: {a_tag}")
    
    url = 'https://www.avito.ru/'
    new_a_tag = re.sub(r'href="[^"]+"', f'href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;"', a_tag)
    
    print(f"New a_tag: {new_a_tag}")
    html = html[:a_start] + new_a_tag + html[a_end:]

    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Logo link updated.")
else:
    print("Could not find href=\"/\"")
