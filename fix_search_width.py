import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the exact string and add ID
target = '<div class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3">'
replacement = '<div id="avito-search-box" class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3" style="width: 100%; grid-column: span 4 / span 4;">'

html = html.replace(target, replacement)

# Update the Javascript logic to handle width as well
# When search is clicked, it shrinks to 75% (or grid column span 3)
js_old_shrink = "if(searchBox) searchBox.style.gridColumn = 'span 3 / span 3';"
js_new_shrink = "if(searchBox) { searchBox.style.gridColumn = 'span 3 / span 3'; searchBox.style.width = 'auto'; }"

# When back is clicked, it expands to 100% (or grid column span 4)
js_old_expand = "if(searchBox) searchBox.style.gridColumn = 'span 4 / span 4';"
js_new_expand = "if(searchBox) { searchBox.style.gridColumn = 'span 4 / span 4'; searchBox.style.width = '100%'; }"

html = html.replace(js_old_shrink, js_new_shrink)
html = html.replace(js_old_expand, js_new_expand)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added avito-search-box ID and updated width logic.")
