import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I want to update the inline style of avito-search-box
old_style = 'style="width: 100%; grid-column: span 4 / span 4;"'
new_style = 'style="flex: 0 0 100% !important; max-width: 100% !important; grid-column: span 4 / span 4 !important;"'
html = html.replace(old_style, new_style)

# I also want to update the Javascript logic so it uses !important when setting 100%
# Find the exact JS code: searchBox.style.width = '100%';
js_width_100_old = "searchBox.style.width = '100%';"
js_width_100_new = "searchBox.style.cssText = 'flex: 0 0 100% !important; max-width: 100% !important; grid-column: span 4 / span 4 !important;';"
html = html.replace(js_width_100_old, js_width_100_new)

# Find the exact JS code: searchBox.style.width = 'auto';
# Wait, if I set cssText, I need to reset it to what it was initially for span 3
js_width_auto_old = "searchBox.style.width = 'auto';"
js_width_auto_new = "searchBox.style.cssText = '';" # This removes inline styles and falls back to styles-module-root_span_3-Fp6fh
html = html.replace(js_width_auto_old, js_width_auto_new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated search box width logic with !important.")
