import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# The grid starts with <div class="ProfileItemsGrid-module-root-wq8JY">
# We want to replace the whole thing or empty its contents.
# Let's find the grid div and the following sibling
grid_start_idx = html.find('<div class="ProfileItemsGrid-module-root-wq8JY">')

if grid_start_idx != -1:
    # Find the next <div> that is a sibling.
    # Actually, the grid contains just one item: <div data-marker="item_list_with_filters/item(0)" ...>
    # If I just use regex to remove that item:
    
    # Let's find item(0)
    item_start = html.find('<div data-marker="item_list_with_filters/item(0)"', grid_start_idx)
    
    if item_start != -1:
        # Find the end of this item. It's a huge block of HTML.
        # Let's just find the closing </div> of the ProfileItemsGrid-module-root-wq8JY by matching the end of the file or the next major section.
        # Actually, if I just replace `<div class="ProfileItemsGrid-module-root-wq8JY">` with `<div class="ProfileItemsGrid-module-root-wq8JY" style="display: none;">` it's much safer!
        
        html = html.replace('<div class="ProfileItemsGrid-module-root-wq8JY">', '<div class="ProfileItemsGrid-module-root-wq8JY" style="display: none;">')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully hid the items grid.")
    else:
        print("Item not found, maybe already empty?")
else:
    print("Grid not found")
