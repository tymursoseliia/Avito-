import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the custom header to be hidden by default and have an ID
custom_header_old = '<div class="custom-avito-header" style="margin-bottom: 24px; font-family: \'Manrope\', Arial, sans-serif;">'
custom_header_new = '<div class="custom-avito-header" id="avito-search-header" style="display: none; margin-bottom: 24px; font-family: \'Manrope\', Arial, sans-serif;">'
html = html.replace(custom_header_old, custom_header_new)

# Update the "Профиль продавца" link to have an ID
profile_link_old = '<a href="#" style="text-decoration: none; color: #000; font-size: 14px; margin-bottom: 16px; display: inline-flex; align-items: center; gap: 4px;">'
profile_link_new = '<a href="#" id="back-to-profile-btn" style="text-decoration: none; color: #000; font-size: 14px; margin-bottom: 16px; display: inline-flex; align-items: center; gap: 4px;">'
html = html.replace(profile_link_old, profile_link_new)


# 2. Inject the original tabs right BEFORE the custom header
original_tabs = """
<div class="styles-module-root-fSK0J" id="avito-original-tabs">
  <div class="styles-module-content-eFVFF">
    <div role="tablist" class="styles-module-tabs-TqDIh" data-marker="extended_profile_tabs">
      <button type="button" role="tab" aria-selected="true" class="styles-module-tab-button-M6XIA styles-module-tab-button_size-xxl-vlm_j styles-module-tab-button_active-mZotZ" data-num="0" data-marker="extended_profile_tabs/tab(active)">
        <span class="styles-module-text-wrapper-H4j4V">
          <span class="styles-module-tab-button-title-aJEVW styles-module-tab-button-title_size-xxl-CaMiQ">Активные</span>
          <span class="styles-module-counter-uAip7 styles-module-counter_size-xxl-QSxPn">65</span>
        </span>
      </button>
      <button type="button" role="tab" aria-selected="false" class="styles-module-tab-button-M6XIA styles-module-tab-button_size-xxl-vlm_j" data-num="1" data-marker="extended_profile_tabs/tab(closed)">
        <span class="styles-module-text-wrapper-H4j4V">
          <span class="styles-module-tab-button-title-aJEVW styles-module-tab-button-title_size-xxl-CaMiQ">Завершённые</span>
          <span class="styles-module-counter-uAip7 styles-module-counter_size-xxl-QSxPn">816</span>
        </span>
      </button>
    </div>
    <div class="styles-module-emphasis-v4zWn"></div>
  </div>
  <div class="styles-module-breakpoint-sdFQO styles-module-breakpoint_m-Z52Hl styles-module-breakpoint_l-_QfHr styles-module-breakpoint_xl-kwUrY styles-module-breakpoint_xxl-O3i8y styles-module-breakpoint_xxxl-BxY8L"></div>
  <div class="styles-module-underline-CxbUx"></div>
</div>
"""
if 'id="avito-original-tabs"' not in html:
    html = html.replace(custom_header_new, original_tabs + custom_header_new)

# 3. Hide the results count bar by default
bar_old = '<div id="results-count-bar" style="display: flex;'
bar_new = '<div id="results-count-bar" style="display: none;'
html = html.replace(bar_old, bar_new)

# 4. Show the items grid by default, and add an ID
grid_old = '<div class="ProfileItemsGrid-module-root-wq8JY" style="display: none;">'
grid_new = '<div class="ProfileItemsGrid-module-root-wq8JY" id="avito-items-grid" style="display: grid;">'
# In case it's not exactly that string, let's use regex
html = re.sub(r'<div class="ProfileItemsGrid-module-root-wq8JY"[^>]*>', grid_new, html)


# 5. Add JavaScript to handle the toggle
# The "Найти" button has data-marker="item_list_with_filters/search_button"
js_logic = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var searchBtn = document.querySelector('[data-marker="item_list_with_filters/search_button"]');
    var backBtn = document.getElementById('back-to-profile-btn');
    
    var originalTabs = document.getElementById('avito-original-tabs');
    var searchHeader = document.getElementById('avito-search-header');
    var resultsBar = document.getElementById('results-count-bar');
    var itemsGrid = document.getElementById('avito-items-grid');
    
    if(searchBtn) {
        searchBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if(originalTabs) originalTabs.style.display = 'none';
            if(searchHeader) searchHeader.style.display = 'block';
            if(resultsBar) resultsBar.style.display = 'flex';
            if(itemsGrid) itemsGrid.style.display = 'none';
        });
    }
    
    if(backBtn) {
        backBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if(originalTabs) originalTabs.style.display = 'block';
            if(searchHeader) searchHeader.style.display = 'none';
            if(resultsBar) resultsBar.style.display = 'none';
            if(itemsGrid) itemsGrid.style.display = 'grid';
        });
    }
});
</script>
</body>
"""

if 'if(originalTabs) originalTabs.style.display' not in html:
    html = html.replace('</body>', js_logic)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added dynamic JS toggle logic and restored initial state.")
