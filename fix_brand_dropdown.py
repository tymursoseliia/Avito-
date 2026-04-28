import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert all wrong replacements
html = html.replace('<div id="brand-dropdown-container" style="position: relative;">', '<div>')

# 2. Add the correct container ID to the specific <div> wrapping the brand-input
marka_input_idx = html.find('id="brand-input"')
if marka_input_idx != -1:
    label_start_idx = html.rfind('<label', 0, marka_input_idx)
    div_start_idx = html.rfind('<div', 0, label_start_idx)
    
    # We slice and insert to guarantee we only change the ONE correct <div>
    div_tag_end = html.find('>', div_start_idx)
    div_tag = html[div_start_idx:div_tag_end+1]
    
    if 'style="' in div_tag:
        new_div_tag = div_tag.replace('style="', 'id="brand-dropdown-container" style="position: relative; ')
    else:
        new_div_tag = div_tag.replace('<div', '<div id="brand-dropdown-container" style="position: relative;"')
    
    html = html[:div_start_idx] + new_div_tag + html[div_tag_end+1:]
    
    # 3. Make the brand-input typable by removing `readonly`
    input_str = html[html.rfind('<input', 0, marka_input_idx):html.find('>', marka_input_idx)+1]
    new_input_str = input_str.replace('readonly ', '').replace('readonly', '')
    html = html.replace(input_str, new_input_str)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed dropdown container and removed readonly.")
