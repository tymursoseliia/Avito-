import re
import json

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('class="ProfileItemsGrid-module-root-wq8JY"')
if start_idx == -1:
    print("Grid not found")
    exit()

# Move back to the <div
start_idx = html.rfind('<div', 0, start_idx)

# We need to find the matching closing div.
i = start_idx
open_divs = 0
first_tag_found = False

while i < len(html):
    if html[i:i+4] == '<div':
        open_divs += 1
        first_tag_found = True
    elif html[i:i+6] == '</div>':
        open_divs -= 1
        
    if first_tag_found and open_divs == 0:
        end_idx = i + 6
        break
    i += 1

if open_divs != 0:
    print("Failed to parse matching divs")
    exit()

grid_full_html = html[start_idx:end_idx]

# Extract just the innerHTML
inner_start = grid_full_html.find('>') + 1
inner_end = grid_full_html.rfind('</div')
grid_inner_html = grid_full_html[inner_start:inner_end]

if "Voyah Taishan" not in grid_inner_html:
    print("Voyah not in inner HTML. Already emptied?")
    exit()

print("Extracted grid inner HTML length:", len(grid_inner_html))

new_grid_html = grid_full_html[:inner_start] + grid_full_html[inner_end:]
html = html.replace(grid_full_html, new_grid_html)

script_idx = html.find('let completedCarsHtml = \'\';')
if script_idx != -1:
    safe_inner_html = json.dumps(grid_inner_html)
    html = html.replace("let completedCarsHtml = '';", f"let completedCarsHtml = {safe_inner_html};")
    html = html.replace("if (!completedCarsHtml) {\n      completedCarsHtml = grid.innerHTML;\n  }", "")

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully extracted static cars to JS variable and emptied the static HTML.")
