import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the old JS logic and replace it.
# The old JS starts with `var brandContainer = document.getElementById('brand-dropdown-container');`
# I'll just write a regex to replace the entire IIFE for the brand menu.

new_js_logic = """
<script>
(function() {
    var brandContainer = document.getElementById('brand-dropdown-container');
    var brandInput = document.getElementById('brand-input');
    var brandMenu = document.getElementById('brand-dropdown-menu');
    
    if (brandContainer && brandInput && brandMenu) {
        var items = brandMenu.querySelectorAll('.brand-item');
        
        // Toggle menu when clicking the container
        brandContainer.addEventListener('click', function(e) {
            e.stopPropagation();
            if (brandMenu.style.display === 'none') {
                brandMenu.style.display = 'block';
                // When opened by clicking, reset filter
                items.forEach(function(item) {
                    item.style.display = 'flex';
                });
            }
        });
        
        // Filter items on typing
        brandInput.addEventListener('input', function(e) {
            e.stopPropagation();
            var filterText = e.target.value.toLowerCase();
            
            // Ensure menu is open when typing
            brandMenu.style.display = 'block';
            
            // Update mirror span to keep layout consistent
            var mirror = brandContainer.querySelector('.styles-module-inputMirror-tflQY');
            if (mirror) mirror.textContent = e.target.value || 'Марка';
            
            items.forEach(function(item) {
                if (item.classList.contains('not-selected')) {
                    item.style.display = 'flex'; // always show "Не выбрано"
                    return;
                }
                var itemText = item.textContent.toLowerCase();
                if (itemText.indexOf(filterText) > -1) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
        
        // Handle selection
        items.forEach(function(item) {
            item.addEventListener('click', function(e) {
                e.stopPropagation();
                var val = item.getAttribute('data-value');
                var text = val || '';
                
                brandInput.value = text;
                var mirror = brandContainer.querySelector('.styles-module-inputMirror-tflQY');
                if (mirror) mirror.textContent = text || 'Марка';
                
                brandMenu.style.display = 'none';
            });
        });
        
        // Close menu when clicking outside
        window.addEventListener('click', function(e) {
            if (brandMenu && brandMenu.style.display === 'block') {
                brandMenu.style.display = 'none';
            }
        });
    }
})();
</script>
"""

# Replace the old JS logic block.
# Since I injected it near the end of the body, I can use a simple regex.
pattern = re.compile(r'<script>\s*\(function\(\) \{\s*var brandContainer = document\.getElementById\(\'brand-dropdown-container\'\);.*?\}\)\(\);\s*</script>', re.DOTALL)

if pattern.search(html):
    html = pattern.sub(new_js_logic.strip(), html)
else:
    print("Could not find the old JS logic to replace.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added typing filter logic to brand dropdown.")
