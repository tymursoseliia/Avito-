with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

old_style = 'id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-top: 12px; margin-bottom: 24px; padding: 0 10px;"'
new_style = 'id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-top: 12px; margin-bottom: 24px; padding: 0;"'

if old_style in html:
    html = html.replace(old_style, new_style)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Padding removed successfully')
else:
    print('Could not find the style string')
