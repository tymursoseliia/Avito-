import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the brand dropdown menu HTML completely
pattern_dropdown = re.compile(r'<div class="custom-brand-dropdown" id="brand-dropdown-menu" style="display: none;">.*?</div>\s*</div>', re.DOTALL)
html = pattern_dropdown.sub('', html)

# 2. Remove the custom JS for the brand dropdown
# We can find the script that contains "brandContainer" and remove it
pattern_js = re.compile(r'<script>\s*\(function\(\) \{\s*var brandContainer = document\.getElementById\(\'brand-dropdown-container\'\);.*?</script>', re.DOTALL)
html = pattern_js.sub('', html)

# 3. Remove all dropdown arrow icons (svgs inside iconAfter-vRsvw) from the filter inputs
# The arrow HTML looks like:
# <span class="styles-module-icon-CkS9m styles-module-iconAfter-vRsvw">
#   <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #8f8f8f; width: 16px; height: 16px;">
#       <polyline points="6 9 12 15 18 9"></polyline>
#   </svg>
# </span>
pattern_arrows = re.compile(r'<span class="styles-module-icon-CkS9m styles-module-iconAfter-vRsvw">\s*<svg.*?<polyline points="6 9 12 15 18 9"></polyline>\s*</svg>\s*</span>', re.DOTALL)
html = pattern_arrows.sub('', html)

# 4. Remove `readonly` from all inputs inside the custom-auto-filters container
# First, let's locate the custom-auto-filters container
start_filters = html.find('id="custom-auto-filters"')
if start_filters != -1:
    end_filters = html.find('Больше фильтров', start_filters)
    # We only want to process inputs inside this section
    filters_html = html[start_filters:end_filters]
    
    # Remove `readonly`
    filters_html = filters_html.replace(' readonly ', ' ').replace('readonly ', '')
    
    # Also remove `cursor: pointer;` from inputs and labels in this section
    filters_html = filters_html.replace('cursor: pointer;', '')
    
    html = html[:start_filters] + filters_html + html[end_filters:]

# Also, there was the "Автомобили" main select near the search bar. Should we remove its arrow too?
# "просто везде можно было писать текс и все" -> Yes, let's remove readonly and arrows from it too!
# Let's just remove `readonly` from ANY input with class="styles-module-input-VLI5k" globally, 
# because all search inputs should be typable now.
html = html.replace('readonly style="font-size: 14px;"', 'style="font-size: 14px;"')
html = html.replace('readonly style="cursor: pointer; font-size: 14px;"', 'style="font-size: 14px;"')
html = html.replace('readonly style="cursor: pointer;"', '')
html = html.replace('readonly', '') # catch any stragglers, though be careful not to break other native avito things. 
# Actually, global readonly removal might be safe since we want to type everywhere.

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed all dropdowns and made inputs typable.")
