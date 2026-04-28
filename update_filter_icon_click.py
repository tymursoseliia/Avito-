import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Update the click listener to also trigger on the filter icon
old_js = """var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
    if (searchBtn) {"""

new_js = """var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
    var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
    if (searchBtn || filterIcon) {"""

html = html.replace(old_js, new_js)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added filter icon click handling.")
