import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hide category box forever
cat_box_old = 'id="avito-category-box"'
cat_box_new = 'id="avito-category-box" style="display: none !important;"'
if 'style="display: none !important;"' not in html[html.find('id="avito-category-box"'):html.find('>', html.find('id="avito-category-box"'))]:
    html = html.replace(cat_box_old, cat_box_new)

# 2. Make search box take full width forever
search_box_old = 'id="avito-search-box" class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3"'
search_box_new = 'id="avito-search-box" class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3" style="flex: 0 0 100% !important; max-width: 100% !important; grid-column: span 4 / span 4 !important;"'
if 'style=' not in html[html.find('id="avito-search-box"'):html.find('>', html.find('id="avito-search-box"'))]:
    html = html.replace(search_box_old, search_box_new)

# 3. Add width: 100% to the form to ensure the gray input stretches
form_old = '<form data-marker="item_list_with_filters/query/form">'
form_new = '<form data-marker="item_list_with_filters/query/form" style="width: 100%; display: flex;">'
html = html.replace(form_old, form_new)

# 4. Add flex: 1 to the label inside the form so it fills the space
label_old = 'data-marker="item_list_with_filters/query/query" tabindex="-1"'
label_new = 'data-marker="item_list_with_filters/query/query" tabindex="-1" style="flex: 1;"'
html = html.replace(label_old, label_new)

# 5. Clean up any dynamic JS that tries to change the width of the search box or toggle category box
# Because now it's PERMANENT.
html = re.sub(r'var catBox = document\.getElementById\(\'avito-category-box\'\);\s*if\(catBox\) catBox\.style\.display = \'[a-z]+\';', '', html)
html = re.sub(r'var searchBox = document\.getElementById\(\'avito-search-box\'\);\s*if\(searchBox\) \{[^}]+\}', '', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied permanent full width to search box and removed category box.")
