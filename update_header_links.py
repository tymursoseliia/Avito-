import sys
import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# For each target, find the enclosing <a> tag
# Since it's a huge minified file, we'll use regex to find the <a> tag right before the text.

targets = {
    'Карьера в Авито': 'https://career.avito.com/?utm_source=avito.ru&utm_medium=referral&utm_campaign=test_placement_to_career&utm_content=top_vacancy',
    'Помощь': 'https://support.avito.ru/',
    '#яПомогаю': 'https://www.avito.ru/avito-care/crisis-help?from=mp_header'
}

for text, url in targets.items():
    # Find the text
    idx = html.find(text)
    if idx != -1:
        # Find the preceding <a
        a_start = html.rfind('<a ', 0, idx)
        a_end = html.find('>', a_start) + 1
        
        a_tag = html[a_start:a_end]
        print(f"Original a_tag for '{text}': {a_tag}")
        
        # We want to replace href="..." and add target="_blank" onclick="..."
        # First, check if there is an href.
        if 'href=' in a_tag:
            new_a_tag = re.sub(r'href="[^"]+"', f'href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;"', a_tag)
        else:
            # If no href, just add it
            new_a_tag = a_tag.replace('<a ', f'<a href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;" ')
        
        print(f"New a_tag for '{text}': {new_a_tag}")
        html = html[:a_start] + new_a_tag + html[a_end:]

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Links updated.")
