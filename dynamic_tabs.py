import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

dynamic_tabs_script = """
<script>
(function() {
    var tablist = document.querySelector('[data-marker="extended_profile_tabs"]');
    var underline = document.querySelector('.styles-module-underline-CxbUx');
    
    if (tablist && underline) {
        var buttons = tablist.querySelectorAll('button[role="tab"]');
        
        // Add transition for smooth animation like in React
        underline.style.transition = 'transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1), width 0.3s cubic-bezier(0.25, 0.1, 0.25, 1)';
        
        function updateUnderline(btn) {
            var width = btn.offsetWidth;
            var offsetLeft = btn.offsetLeft;
            underline.style.width = width + 'px';
            underline.style.transform = 'translateX(' + offsetLeft + 'px)';
        }
        
        buttons.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                // Deactivate all
                buttons.forEach(function(b) {
                    b.setAttribute('aria-selected', 'false');
                    b.classList.remove('styles-module-tab-button_active-mZotZ');
                });
                
                // Activate clicked
                btn.setAttribute('aria-selected', 'true');
                btn.classList.add('styles-module-tab-button_active-mZotZ');
                
                // Move underline
                updateUnderline(btn);
            });
        });
        
        // Initialize position on load
        window.addEventListener('load', function() {
            var activeBtn = tablist.querySelector('button[aria-selected="true"]');
            if (activeBtn) {
                updateUnderline(activeBtn);
            }
        });
        
        // Fallback if load event already fired
        setTimeout(function() {
            var activeBtn = tablist.querySelector('button[aria-selected="true"]');
            if (activeBtn) {
                updateUnderline(activeBtn);
            }
        }, 100);
    }
})();
</script>
"""

# Append before </body>
idx = html.rfind('</body>')
if idx != -1:
    html = html[:idx] + dynamic_tabs_script + html[idx:]

# Remove the hardcoded style from my previous script so it doesn't conflict with the dynamic logic
old_underline = '<div class="styles-module-underline-CxbUx" style="width: 132px; transform: translateX(0px);"></div>'
new_underline = '<div class="styles-module-underline-CxbUx" style="background-color: #000; height: 2px; position: absolute; bottom: 0; left: 0; border-radius: 2px;"></div>'

if old_underline in html:
    html = html.replace(old_underline, new_underline)
else:
    # Just in case it wasn't there exactly as expected
    old_underline2 = '<div class="styles-module-underline-CxbUx"></div>'
    html = html.replace(old_underline2, new_underline)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added dynamic tab script and refined underline styles.")
