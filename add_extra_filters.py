import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

def make_avito_dropdown(placeholder):
    return f'''
    <label class="styles-module-root-xMJB7 styles-module-root_size-m-m1EB0 styles-module-root_empty-DO6zB" tabindex="-1" style="cursor: pointer; width: 100%;">
      <div class="styles-module-contentWrapper-H7tid">
        <div class="styles-module-content-mMdg8">
          <div class="styles-module-inputWrapper-ElVit styles-module-inputWrapper_fullWidth-vAlp5">
            <input class="styles-module-input-VLI5k" placeholder="{placeholder}" readonly style="cursor: pointer; font-size: 14px;">
            <span class="styles-module-inputMirror-tflQY" style="visibility: hidden;">{placeholder}</span>
          </div>
        </div>
      </div>
      <span class="styles-module-icon-CkS9m styles-module-iconAfter-vRsvw">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #8f8f8f; width: 16px; height: 16px;">
            <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </span>
    </label>
    '''

def make_avito_input(placeholder):
    return f'''
    <label class="styles-module-root-xMJB7 styles-module-root_size-m-m1EB0 styles-module-root_empty-DO6zB" tabindex="-1" style="width: 100%;">
      <div class="styles-module-contentWrapper-H7tid">
        <div class="styles-module-content-mMdg8">
          <div class="styles-module-inputWrapper-ElVit styles-module-inputWrapper_fullWidth-vAlp5">
            <input class="styles-module-input-VLI5k" placeholder="{placeholder}" style="font-size: 14px;">
            <span class="styles-module-inputMirror-tflQY" style="visibility: hidden;">{placeholder}</span>
          </div>
        </div>
      </div>
    </label>
    '''

extra_filters_html = f'''
  <div id="extra-filters" style="display: none;">
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 8px;">
        <div>{make_avito_input("от")}</div>
        <div>{make_avito_input("до")}</div>
        <div>{make_avito_dropdown("Коробка передач")}</div>
      </div>
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 8px; margin-bottom: 8px;">
        <div>{make_avito_dropdown("Состояние")}</div>
        <div>{make_avito_dropdown("Тип двигателя")}</div>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 8px;">
        <div>{make_avito_dropdown("Объём двигателя от, л")}</div>
        <div>{make_avito_dropdown("Объём двигателя до, л")}</div>
        <div>{make_avito_dropdown("Тип кузова")}</div>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 8px;">
        <div>{make_avito_dropdown("Пробег от, тыс. км")}</div>
        <div>{make_avito_dropdown("Пробег до, тыс. км")}</div>
        <div>{make_avito_dropdown("Привод")}</div>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 8px; margin-bottom: 12px;">
        <div>{make_avito_dropdown("Руль")}</div>
        <div></div>
      </div>
  </div>
'''

# We need to replace the current "Больше фильтров" button with a new one that has an ID.
old_more_filters = '''<div style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000;">
    Больше фильтров <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>
  </div>'''

new_more_filters = f'''{extra_filters_html}
  <div id="more-filters-btn" style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000;">
    <span>Больше фильтров</span> <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>
  </div>'''

# Let's verify exactly how old_more_filters is written in the file so we don't miss the replacement.
idx = html.find('Больше фильтров')
start_idx = html.rfind('<div', 0, idx)
end_idx = html.find('</div>', idx) + 6
actual_old_more_filters = html[start_idx:end_idx]

html = html.replace(actual_old_more_filters, new_more_filters)

# Add JS logic for toggling extra-filters
extra_js = """
<script>
(function() {
    window.addEventListener('click', function(e) {
        var moreBtn = e.target.closest('#more-filters-btn');
        if (moreBtn) {
            e.preventDefault();
            e.stopPropagation();
            var extraFilters = document.getElementById('extra-filters');
            var textSpan = moreBtn.querySelector('span:first-child');
            var arrowSpan = moreBtn.querySelector('span:last-child');
            if (extraFilters) {
                if (extraFilters.style.display === 'none') {
                    extraFilters.style.display = 'block';
                    textSpan.textContent = 'Меньше фильтров';
                    arrowSpan.textContent = '^';
                } else {
                    extraFilters.style.display = 'none';
                    textSpan.textContent = 'Больше фильтров';
                    arrowSpan.textContent = '⌄';
                }
            }
        }
    }, true);
})();
</script>
"""

if 'more-filters-btn' in new_more_filters and 'getElementById(\'extra-filters\')' not in html:
    html = html.replace('</body>', extra_js + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Extra filters added.")
