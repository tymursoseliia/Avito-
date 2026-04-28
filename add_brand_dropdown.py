import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for the dropdown
dropdown_css = """
<style>
.custom-brand-dropdown {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    width: 100%;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    z-index: 1000;
    font-family: Manrope, sans-serif;
    font-size: 14px;
    color: #000;
    overflow-y: auto;
    max-height: 300px;
}
.brand-item {
    padding: 10px 16px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.brand-item:hover {
    background-color: #f2f2f2;
}
.brand-title {
    padding: 12px 16px 8px;
    font-weight: 700;
    color: #000;
}
.brand-item.not-selected {
    background-color: #f2f2f2;
}
</style>
"""

# HTML for the dropdown menu
dropdown_html = """
<div class="custom-brand-dropdown" id="brand-dropdown-menu" style="display: none;">
   <div class="brand-item not-selected" data-value="">
     <span>Не выбрано</span>
     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"></polyline>
     </svg>
   </div>
   <div class="brand-title">Популярные</div>
   <div class="brand-item" data-value="Audi">Audi</div>
   <div class="brand-item" data-value="BMW">BMW</div>
   <div class="brand-item" data-value="Chery">Chery</div>
   <div class="brand-item" data-value="Chevrolet">Chevrolet</div>
   <div class="brand-item" data-value="Ford">Ford</div>
   <div class="brand-item" data-value="Hyundai">Hyundai</div>
   <div class="brand-item" data-value="Kia">Kia</div>
   <div class="brand-item" data-value="Lada (ВАЗ)">Lada (ВАЗ)</div>
   <div class="brand-item" data-value="Mercedes-Benz">Mercedes-Benz</div>
   <div class="brand-item" data-value="Nissan">Nissan</div>
   <div class="brand-item" data-value="Renault">Renault</div>
   <div class="brand-item" data-value="Toyota">Toyota</div>
   <div class="brand-item" data-value="Volkswagen">Volkswagen</div>
</div>
"""

# We need to find the "Марка" input and modify its container.
# The container is `<div>{make_avito_dropdown("Марка")}</div>`
# In `clean_avito (1).html`, it looks like:
# <div>
#    <label ...>
#      ...
#      <input class="styles-module-input-VLI5k" placeholder="Марка" readonly style="...">
#      ...
#    </label>
# </div>

# Let's find the exact block for "Марка"
marka_input_idx = html.find('placeholder="Марка"')

if marka_input_idx != -1:
    # Find the opening label tag before it
    label_start_idx = html.rfind('<label', 0, marka_input_idx)
    # Find the opening div tag before the label
    div_start_idx = html.rfind('<div', 0, label_start_idx)
    
    # We want to add `id="marka-container" style="position: relative;"` to the div
    # And `id="brand-input"` to the input
    
    # Let's replace the input to add ID
    input_str = html[html.rfind('<input', 0, marka_input_idx):html.find('>', marka_input_idx)+1]
    new_input_str = input_str.replace('<input ', '<input id="brand-input" ')
    html = html.replace(input_str, new_input_str)
    
    # Now let's find the container div. It's inside a grid.
    # The grid looks like: `<div style="display: grid; ..."> \n <div> \n <label ...`
    # Let's find the label again after input replacement
    marka_input_idx = html.find('id="brand-input"')
    label_start_idx = html.rfind('<label', 0, marka_input_idx)
    div_start_idx = html.rfind('<div', 0, label_start_idx)
    
    # Replace the `<div` with `<div id="brand-dropdown-container" style="position: relative;"`
    # Wait, the div might already have a style or class. Let's get the tag.
    div_tag_end = html.find('>', div_start_idx)
    div_tag = html[div_start_idx:div_tag_end+1]
    
    if 'style="' in div_tag:
        new_div_tag = div_tag.replace('style="', 'id="brand-dropdown-container" style="position: relative; ')
    else:
        new_div_tag = div_tag.replace('<div', '<div id="brand-dropdown-container" style="position: relative;"')
    
    html = html.replace(div_tag, new_div_tag)
    
    # Now insert the dropdown_html right after the closing </label> of this specific block.
    # The label ends at:
    label_end_idx = html.find('</label>', marka_input_idx) + 8
    html = html[:label_end_idx] + '\n' + dropdown_html + html[label_end_idx:]

# Insert CSS into <head>
if 'custom-brand-dropdown' not in html:
    html = html.replace('</head>', dropdown_css + '\n</head>')

# Insert JS logic
js_logic = """
<script>
(function() {
    var brandContainer = document.getElementById('brand-dropdown-container');
    var brandInput = document.getElementById('brand-input');
    var brandMenu = document.getElementById('brand-dropdown-menu');
    
    if (brandContainer && brandInput && brandMenu) {
        // Toggle menu when clicking the input/container
        brandContainer.addEventListener('click', function(e) {
            // Prevent closing immediately from window click
            e.stopPropagation();
            
            if (brandMenu.style.display === 'none') {
                brandMenu.style.display = 'block';
            } else {
                brandMenu.style.display = 'none';
            }
        });
        
        // Handle selection
        var items = brandMenu.querySelectorAll('.brand-item');
        items.forEach(function(item) {
            item.addEventListener('click', function(e) {
                e.stopPropagation();
                var val = item.getAttribute('data-value');
                var text = val || '';
                
                brandInput.value = text;
                // Also update the mirror text span if needed
                var mirror = brandContainer.querySelector('.styles-module-inputMirror-tflQY');
                if (mirror) mirror.textContent = text;
                
                // Add/remove checkmark logically (just visual for now, we leave the checkmark on 'Не выбрано' to match screenshot, or move it)
                // Let's hide the menu
                brandMenu.style.display = 'none';
            });
        });
        
        // Close menu when clicking outside
        window.addEventListener('click', function(e) {
            if (brandMenu.style.display === 'block') {
                brandMenu.style.display = 'none';
            }
        });
    }
})();
</script>
"""

if 'getElementById(\'brand-dropdown-menu\')' not in html:
    html = html.replace('</body>', js_logic + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Brand dropdown script successfully applied.")
