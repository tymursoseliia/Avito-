import sys
import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

targets = {
    'Авто': 'https://www.avito.ru/all/transport?cd=1',
    'Недвижимость': 'https://www.avito.ru/all/nedvizhimost?cd=1',
    'Работа': 'https://www.avito.ru/all/rabota?cd=1',
    'Услуги': 'https://www.avito.ru/all/predlozheniya_uslug?cd=1'
}

for text, url in targets.items():
    # Find the text in the HTML
    # We want to find occurrences of the text that are inside the navigation menu.
    # The screenshot shows them as a row of links.
    # They should be inside <a> tags.
    # We can search for >Авто< or similar, or just find the text and replace the enclosing a tag.
    
    # We might have multiple occurrences of "Авто", so let's find one that's a link in the header.
    # A good heuristic is to look for the one with data-marker="category-xxx" or similar, 
    # but let's just find the first one that is inside an <a> tag and looks like a menu item.
    
    # Let's find all occurrences of the text
    start_search = 0
    while True:
        idx = html.find(text, start_search)
        if idx == -1:
            print(f"Could not find valid <a> tag for '{text}'")
            break
            
        a_start = html.rfind('<a ', 0, idx)
        a_end = html.find('>', a_start) + 1
        
        # Make sure it's actually an <a> tag wrapping our text (no other </a> in between)
        if html.find('</a>', a_start, idx) == -1:
            a_tag = html[a_start:a_end]
            print(f"Found a_tag for '{text}': {a_tag}")
            
            # Replace
            if 'href=' in a_tag:
                new_a_tag = re.sub(r'href="[^"]+"', f'href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;"', a_tag)
            else:
                new_a_tag = a_tag.replace('<a ', f'<a href="{url}" target="_blank" onclick="window.open(\'{url}\', \'_blank\'); return false;" ')
            
            html = html[:a_start] + new_a_tag + html[a_end:]
            print(f"Updated '{text}'")
            break
        else:
            start_search = idx + len(text)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Sub-menu links updated.")
