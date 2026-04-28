import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the entire custom-auto-filters div with a new one that uses native Avito classes.
# The user's screenshot has `grid-column: 1 / span 6;` for a wrapper, implying a 12-column grid or similar.
# For simplicity, I'll use my existing grid layout but wrap the inputs in the native Avito classes.

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

new_filters_html = f'''<div id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-bottom: 24px; padding: 0 10px;">
  <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 8px; margin-bottom: 8px;">
    <div>{make_avito_dropdown("Тип автомобиля")}</div>
    <div>{make_avito_input("Цена от, ₽")}</div>
    <div>{make_avito_input("Цена до, ₽")}</div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div>{make_avito_dropdown("Марка")}</div>
    <div>{make_avito_dropdown("Модель")}</div>
    <div>{make_avito_dropdown("Поколение")}</div>
  </div>
  <div style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000;">
    Больше фильтров <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>
  </div>
</div>'''

# Find and replace the old custom-auto-filters div
pattern = re.compile(r'<div id="custom-auto-filters" class="custom-auto-filters-container".*?</div>\s*</div>\s*</div>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(new_filters_html, html)
else:
    print("Could not find the old custom-auto-filters block via regex.")
    # Try a more manual approach if regex fails. Let's just find the index of id="custom-auto-filters" and the index of the next <div class="ProfileItemsGrid
    start_idx = html.find('<div id="custom-auto-filters"')
    end_idx = html.find('<div class="ProfileItemsGrid-module-root-wq8JY">')
    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + new_filters_html + '\n' + html[end_idx:]


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced filters with native classes.")
