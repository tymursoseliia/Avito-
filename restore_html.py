import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

with open('missing_part.txt', 'r', encoding='utf-8') as f:
    missing_part = f.read()

# Make the missing part look like item(0)
missing_part_0 = missing_part.replace('item_list_with_filters/item(1)', 'item_list_with_filters/item(0)')

# We need to prepend `<div class="ProfileItemsGrid-module-root-wq8JY"><div data-marker="`
restored_html = '<div class="ProfileItemsGrid-module-root-wq8JY">\n<div data-marker="' + missing_part_0

# The broken place in the HTML is exactly at:
# `</div></div></div></div></div></div></div></div><div class="iva-item-body-D1zaw">`
# Wait, let's look at `custom-auto-filters` to find the exact place to inject.

# Find the end of `custom-auto-filters`
idx = html.find('custom-auto-filters')
# Find the next `<div class="iva-item-body-D1zaw">`
body_idx = html.find('<div class="iva-item-body-D1zaw">', idx)

if body_idx != -1:
    # There are some `</div>` tags between `custom-auto-filters` and `iva-item-body-D1zaw`.
    # Let's just find the closing `</div>` of `custom-auto-filters` container.
    # We know `custom-auto-filters` has a known structure. It ends with:
    # `Больше фильтров <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>\n  </div>\n</div>`
    
    end_of_filters = html.find('Больше фильтров', idx)
    end_of_filters = html.find('</div>', end_of_filters)
    end_of_filters = html.find('</div>', end_of_filters + 1) + 6 # End of custom-auto-filters
    
    # We replace everything from end_of_filters to body_idx with `restored_html`!
    html = html[:end_of_filters] + '\n' + restored_html + html[body_idx:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML restored.")
