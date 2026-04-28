import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert the two new hidden badges
new_badges = """
  <div class="custom-extra-trust" style="display: none; align-items: center; background-color: #E6F6FF; border-radius: 12px; padding: 12px 16px; gap: 12px; margin-top: 8px;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
    <span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">Документы проверены</span>
  </div>
  <div class="custom-extra-trust" style="display: none; align-items: center; background-color: #E6F6FF; border-radius: 12px; padding: 12px 16px; gap: 12px; margin-top: 8px;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
    <span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">Телефон подтверждён</span>
  </div>
"""

# Find the end of the Реквизиты проверены div
target_str = '<span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">Реквизиты проверены</span>\n  </div>'
if target_str in html and new_badges not in html:
    html = html.replace(target_str, target_str + new_badges)
else:
    # Just in case there are no newlines
    target_str_2 = 'Реквизиты проверены</span></div>'
    if target_str_2 in html and new_badges not in html:
        html = html.replace(target_str_2, target_str_2 + new_badges)
    else:
        # regex approach
        if "Документы проверены" not in html:
            html = re.sub(r'(Реквизиты проверены</span>\s*</div>)', r'\1' + new_badges, html)

# 2. Add Javascript to handle the toggle
# We'll inject it before </body> just like the dropdown script
js_code = """
<script>
(function() {
    // Add click listener for "Показать все"
    window.addEventListener('click', function(e) {
        var showMoreBtn = e.target.closest('[data-marker="show-more"]');
        if (showMoreBtn) {
            e.preventDefault();
            e.stopPropagation();
            
            var badges = document.querySelectorAll('.custom-extra-trust');
            var isHidden = true;
            
            badges.forEach(function(badge) {
                if (badge.style.display === 'none') {
                    badge.style.display = 'flex';
                    isHidden = false;
                } else {
                    badge.style.display = 'none';
                    isHidden = true;
                }
            });
            
            // Change button text and arrow
            var textElem = showMoreBtn.querySelector('p');
            var svgElem = showMoreBtn.querySelector('svg');
            
            if (textElem) {
                if (!isHidden) {
                    textElem.textContent = 'Скрыть';
                    if (svgElem) svgElem.style.transform = 'rotate(180deg)';
                } else {
                    textElem.textContent = 'Показать все';
                    if (svgElem) svgElem.style.transform = 'rotate(0deg)';
                }
            }
        }
    }, true);
})();
</script>
</body>
"""

html = html.replace('</body>', js_code)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Badges and JS injected.")
