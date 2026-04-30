import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

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

if 'Документы проверены' not in html:
    html = re.sub(r'(Реквизиты.*?проверены</span>\s*</div>)', r'\1\n' + new_badges, html, flags=re.DOTALL)

js_code = """
<script>
(function() {
    window.addEventListener('click', function(e) {
        var showMoreBtn = e.target.closest('[data-marker="show-more"]');
        if (showMoreBtn) {
            e.preventDefault();
            e.stopPropagation();
            
            var badges = document.querySelectorAll('.custom-extra-trust');
            if (badges.length === 0) return;
            
            var isHidden = badges[0].style.display === 'none';
            
            badges.forEach(function(badge) {
                if (isHidden) {
                    badge.style.display = 'flex';
                } else {
                    badge.style.display = 'none';
                }
            });
            
            var textElem = showMoreBtn.querySelector('p');
            var svgElem = showMoreBtn.querySelector('svg');
            
            if (textElem) {
                if (isHidden) {
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
"""

if 'custom-extra-trust' not in html:
    print('Failed to insert HTML')
else:
    if 'showMoreBtn = e.target.closest' not in html:
        html = html.replace('</body>', js_code + '\n</body>')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Success')
