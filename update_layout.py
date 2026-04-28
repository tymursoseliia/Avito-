import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# The target div to change from span_4 to span_3
old_div = '<div class="styles-module-root-boFHT styles-module-root_span_4-c4Vny styles-module-root_compensation_none-fjYO3">'
new_div = '<div class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3">'

# The new HTML to inject before the new span_3 div
# Note: I am using the standard Avito search input classes for the "Автомобили" label
injected_html = """
<div class="styles-module-root-boFHT styles-module-root_span_1-mrCzn styles-module-root_compensation_none-fjYO3">
  <label class="styles-module-root-xMJB7 styles-module-root_size-m-m1EB0" data-marker="item_list_with_filters/category_select" aria-disabled="false" tabindex="-1">
    <div class="styles-module-contentWrapper-H7tid">
      <div class="styles-module-content-mMdg8">
        <div class="styles-module-inputWrapper-ElVit styles-module-inputWrapper_fullWidth-vAlp5">
          <input marker="item_list_with_filters/category_select" aria-haspopup="true" aria-expanded="false" class="styles-module-input-VLI5k" data-marker="item_list_with_filters/category_select/input" value="Автомобили" readonly style="cursor: pointer; font-size: 14px;">
          <span class="styles-module-inputMirror-tflQY" style="visibility: hidden;">Автомобили</span>
        </div>
      </div>
    </div>
    <span class="styles-module-icon-CkS9m styles-module-iconAfter-vRsvw" style="color: #000;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="3" width="7" height="7"></rect>
        <rect x="14" y="3" width="7" height="7"></rect>
        <rect x="14" y="14" width="7" height="7"></rect>
        <rect x="3" y="14" width="7" height="7"></rect>
      </svg>
    </span>
  </label>
</div>
"""

# Replace the old span_4 with the injected html + the new span_3
if old_div in html:
    html = html.replace(old_div, injected_html + new_div)

# Now, the user screenshot also shows that the search bar now has a left icon instead of the magnifying glass inside it?
# Wait, in Screenshot 1, search bar has a magnifying glass on the left inside the input.
# In Screenshot 2, the search bar STILL has a magnifying glass inside the input.
# So I don't need to remove it.

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Layout updated 1 to 1.")
