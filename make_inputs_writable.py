import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace custom-filter-text spans with inputs
def replace_span(match):
    text = match.group(1)
    return f'<input type="text" placeholder="{text}" style="border: none; background: transparent; width: 100%; outline: none; font-size: 14px; font-family: Manrope, sans-serif; color: #000;">'

html = re.sub(r'<span class="custom-filter-text">(.*?)</span>', replace_span, html)

# 2. Remove readonly from original inputs
html = html.replace('readonly style="cursor: pointer;', 'style="cursor: text;')
html = html.replace('readonly', '')

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated all filter items to be writable inputs.')
