import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to completely rewrite the dropdown CSS and HTML to match the screenshot.
# Background color for "Не выбрано" in screenshot is exactly #E8E5DF (approx).
# Hover background for other items is likely #F2F2F2.

new_css = """
<style>
.custom-brand-dropdown {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    width: 100%;
    background: #ffffff;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    font-size: 14px;
    color: #000;
    overflow-y: auto;
    max-height: 280px;
    border: 1px solid #e0e0e0;
}
.custom-brand-dropdown::-webkit-scrollbar {
    width: 8px;
}
.custom-brand-dropdown::-webkit-scrollbar-thumb {
    background-color: #c4c4c4;
    border-radius: 4px;
}
.brand-item {
    padding: 10px 16px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    line-height: 1.4;
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
    background-color: #e8e5df;
}
.brand-item.not-selected:hover {
    background-color: #e8e5df;
}
</style>
"""

new_dropdown_html = """
<div class="custom-brand-dropdown" id="brand-dropdown-menu" style="display: none;">
   <div class="brand-item not-selected" data-value="">
     <span class="Option-module-label-B3Icr">Не выбрано</span>
     <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="color: #000;">
        <polyline points="20 6 9 17 4 12"></polyline>
     </svg>
   </div>
   <div class="brand-title">Популярные</div>
   <div class="brand-item" data-value="Audi"><span class="Option-module-label-B3Icr">Audi</span></div>
   <div class="brand-item" data-value="BMW"><span class="Option-module-label-B3Icr">BMW</span></div>
   <div class="brand-item" data-value="Chery"><span class="Option-module-label-B3Icr">Chery</span></div>
   <div class="brand-item" data-value="Chevrolet"><span class="Option-module-label-B3Icr">Chevrolet</span></div>
   <div class="brand-item" data-value="Ford"><span class="Option-module-label-B3Icr">Ford</span></div>
   <div class="brand-item" data-value="Hyundai"><span class="Option-module-label-B3Icr">Hyundai</span></div>
   <div class="brand-item" data-value="Kia"><span class="Option-module-label-B3Icr">Kia</span></div>
   <div class="brand-item" data-value="Lada (ВАЗ)"><span class="Option-module-label-B3Icr">Lada (ВАЗ)</span></div>
   <div class="brand-item" data-value="Mercedes-Benz"><span class="Option-module-label-B3Icr">Mercedes-Benz</span></div>
   <div class="brand-item" data-value="Nissan"><span class="Option-module-label-B3Icr">Nissan</span></div>
   <div class="brand-item" data-value="Renault"><span class="Option-module-label-B3Icr">Renault</span></div>
   <div class="brand-item" data-value="Toyota"><span class="Option-module-label-B3Icr">Toyota</span></div>
   <div class="brand-item" data-value="Volkswagen"><span class="Option-module-label-B3Icr">Volkswagen</span></div>
</div>
"""

# Replace old CSS
pattern_css = re.compile(r'<style>\s*\.custom-brand-dropdown \{.*?</style>', re.DOTALL)
if pattern_css.search(html):
    html = pattern_css.sub(new_css.strip(), html)
else:
    print("Could not find CSS to replace.")

# Replace old HTML
pattern_html = re.compile(r'<div class="custom-brand-dropdown" id="brand-dropdown-menu" style="display: none;">.*?</div>\s*</div>\s*<script>', re.DOTALL)
if pattern_html.search(html):
    # Wait, the regex `.*?</div>` might be dangerous if there are nested divs. 
    # Let's use a safer approach for the HTML replacement.
    pass

# Safe HTML replacement
start_idx = html.find('<div class="custom-brand-dropdown" id="brand-dropdown-menu"')
if start_idx != -1:
    end_idx = html.find('</div>\n</div>\n', start_idx)
    # The dropdown ends right before another div usually, but let's just find "Volkswagen</div>\n</div>"
    volk_idx = html.find('Volkswagen</div>', start_idx)
    if volk_idx != -1:
        end_idx = html.find('</div>', volk_idx + 16) + 6
        html = html[:start_idx] + new_dropdown_html.strip() + html[end_idx:]
else:
    print("Could not find HTML dropdown to replace.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Dropdown design updated.")
