import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the #more-filters-btn HTML
new_btn_html = '''<div id="more-filters-btn" style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000; display: inline-flex; align-items: center;">
    <span class="more-filters-text" style="margin-right: 4px;">Больше фильтров</span>
    <svg class="more-filters-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s ease;">
        <polyline points="6 9 12 15 18 9"></polyline>
    </svg>
  </div>'''

# The old HTML looks like:
# <div id="more-filters-btn" style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000;">
#    <span>Больше фильтров</span> <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>
#  </div>
pattern_btn = re.compile(r'<div id="more-filters-btn".*?</div>', re.DOTALL)
html = pattern_btn.sub(new_btn_html, html)


# 2. Update the JS logic
old_js_start = html.find('var moreBtn = e.target.closest(\'#more-filters-btn\');')
if old_js_start != -1:
    # We need to replace the logic inside `if (moreBtn) { ... }`
    js_block_end = html.find('        }\n    }, true);', old_js_start)
    if js_block_end != -1:
        new_js = """var moreBtn = e.target.closest('#more-filters-btn');
        if (moreBtn) {
            e.preventDefault();
            e.stopPropagation();
            var extraFilters = document.getElementById('extra-filters');
            var textSpan = moreBtn.querySelector('.more-filters-text');
            var arrowSvg = moreBtn.querySelector('.more-filters-arrow');
            if (extraFilters) {
                if (extraFilters.style.display === 'none') {
                    extraFilters.style.display = 'block';
                    if (textSpan) textSpan.textContent = 'Меньше фильтров';
                    if (arrowSvg) arrowSvg.style.transform = 'rotate(180deg)';
                } else {
                    extraFilters.style.display = 'none';
                    if (textSpan) textSpan.textContent = 'Больше фильтров';
                    if (arrowSvg) arrowSvg.style.transform = 'rotate(0deg)';
                }
            }
"""
        html = html[:old_js_start] + new_js + html[js_block_end:]


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated more-filters-btn UI and logic.")
