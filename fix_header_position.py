import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the custom-search-header
header_regex = r'<div id="custom-search-header".*?</h1>\s*</div>'
header_match = re.search(header_regex, html, flags=re.DOTALL)
if header_match:
    header_html = header_match.group(0)
    # Remove it from its current location
    html = html.replace(header_html, '')
    
    # 2. Find the target grid container
    target_container_str = '<div class="styles-module-root-xEbQv styles-module-root_columns_4-SJwlR"'
    target_pos = html.find(target_container_str)
    
    if target_pos != -1:
        # Insert it before the grid container
        html = html[:target_pos] + header_html + '\n' + html[target_pos:]
        print('Moved custom-search-header successfully')
    else:
        print('Could not find target grid container')
else:
    print('Could not find custom-search-header')

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
