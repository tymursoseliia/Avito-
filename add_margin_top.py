import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

old_style = '<div id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-bottom: 24px; padding: 0 10px;">'
new_style = '<div id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-top: 12px; margin-bottom: 24px; padding: 0 10px;">'

html = html.replace(old_style, new_style)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Added margin-top: 12px')
