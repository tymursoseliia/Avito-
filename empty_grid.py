import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I want to empty the <div class="ProfileItemsGrid-module-root-wq8JY"> ... </div>
# The grid starts here
grid_start = '<div class="ProfileItemsGrid-module-root-wq8JY">'
idx_start = html.find(grid_start)

if idx_start != -1:
    # Let's find the closing div of the grid.
    # It's followed by some standard pagination or footer.
    # The safest way is to regex match the content inside the grid up to a known element,
    # or just use a simple parsing logic.
    # Let's find the first data-marker="item_list_with_filters/item(0)"
    item_start = html.find('<div data-marker="item_list_with_filters/item(0)"', idx_start)
    if item_start != -1:
        # The grid closes right before <div class="styles-module-root-a20_T" ... which is pagination
        pagination_start = html.find('<div class="styles-module-root-a20_T"', item_start)
        if pagination_start != -1:
            # We replace everything between grid_start + len(grid_start) and pagination_start
            # with just a closing </div> (if it was part of the grid, actually pagination is a sibling)
            # Let's look for the </div> that closes the grid.
            # It's right before pagination_start.
            # To be very safe, let's just delete the string from item_start up to pagination_start, 
            # minus the </div>
            # Actually, I'll just remove the item(0) div completely using regex
            # Or simpler:
            item_end = html.find('<div class="styles-module-root-a20_T"', item_start)
            # Find the last </div> before pagination
            last_div = html.rfind('</div>', item_start, item_end)
            
            # Delete from item_start to last_div
            html = html[:item_start] + html[last_div:]
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html)
            print("Successfully emptied the items grid.")
        else:
            print("Pagination not found")
    else:
        print("Item not found")
else:
    print("Grid not found")
