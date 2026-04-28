import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject custom search header above the search bar
header_html = """
<div id="custom-search-header" style="display: none; margin-bottom: 24px; font-family: 'Manrope', Arial, sans-serif;">
  <a href="#" id="search-back-btn" style="text-decoration: none; color: #000; font-size: 14px; margin-bottom: 24px; display: inline-flex; align-items: center; gap: 4px;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
    Профиль продавца
  </a>
  <h1 style="font-size: 32px; font-weight: 800; margin: 0; color: #000; display: flex; justify-content: space-between; align-items: center;">
    Объявления
    <div style="font-size: 14px; font-weight: 400; display: flex; align-items: center; gap: 4px; cursor: pointer;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
      Все регионы
    </div>
  </h1>
</div>
"""

# Find the search bar container's wrapper and insert header before it
search_wrapper_start = html.find('<div class="styles-module-root-boFHT')
if search_wrapper_start != -1 and 'id="custom-search-header"' not in html:
    html = html[:search_wrapper_start] + header_html + html[search_wrapper_start:]


# 2. Inject "Автомобили" button into the search flex container
cat_btn_html = """
<div id="search-category-btn" style="display: none; background: #f2f2f2; border-radius: 8px; padding: 0 16px; height: 48px; align-items: center; gap: 8px; cursor: pointer; margin-right: 8px; flex-shrink: 0;">
  <span style="font-size: 14px; font-family: Manrope, sans-serif;">Автомобили</span>
  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4 4h4v4H4V4zm6 0h4v4h-4V4zm6 0h4v4h-4V4zM4 10h4v4H4v-4zm6 0h4v4h-4v-4zm6 0h4v4h-4v-4zM4 16h4v4H4v-4zm6 0h4v4h-4v-4zm6 0h4v4h-4v-4z"/></svg>
</div>
"""

search_inner = html.find('<div class="styles-module-root-jjade')
if search_inner != -1 and 'id="search-category-btn"' not in html:
    insert_pos = html.find('>', search_inner) + 1
    html = html[:insert_pos] + cat_btn_html + html[insert_pos:]


# 3. Add JS toggle logic replacing the previous one
old_js = """        var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        
        if (searchBtn || filterIcon) {
            e.preventDefault();
            e.stopPropagation();
            var filterMenu = document.getElementById('custom-auto-filters');
            if (filterMenu) {
                if (filterMenu.style.display === 'none') {
                    filterMenu.style.display = 'block';
                } else {
                    filterMenu.style.display = 'none';
                }
            }
        }"""

new_js = """        var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        var backBtn = e.target.closest('#search-back-btn');
        
        var customHeader = document.getElementById('custom-search-header');
        var catBtn = document.getElementById('search-category-btn');
        var filterMenu = document.getElementById('custom-auto-filters');
        
        // Find the tabs wrapper. It's the previous sibling element of the search wrapper generally.
        var tabsElement = document.querySelector('.styles-module-root-fSK0J');
        
        if (searchBtn || filterIcon) {
            e.preventDefault();
            e.stopPropagation();
            
            // Show new UI state
            if (tabsElement) tabsElement.style.display = 'none';
            if (customHeader) customHeader.style.display = 'block';
            if (catBtn) catBtn.style.display = 'flex';
            if (filterMenu) filterMenu.style.display = 'block';
        }
        
        if (backBtn) {
            e.preventDefault();
            e.stopPropagation();
            
            // Revert UI state
            if (tabsElement) tabsElement.style.display = 'block';
            if (customHeader) customHeader.style.display = 'none';
            if (catBtn) catBtn.style.display = 'none';
            if (filterMenu) filterMenu.style.display = 'none';
        }"""

html = html.replace(old_js, new_js)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied search state transitions successfully.")
