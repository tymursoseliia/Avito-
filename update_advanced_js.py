import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add ID to the category box "Автомобили"
# It looks like: <div class="styles-module-root-boFHT styles-module-root_span_1-mrCzn styles-module-root_compensation_none-fjYO3">
# Followed by <label ... data-marker="item_list_with_filters/category_select"
cat_idx = html.find('item_list_with_filters/category_select')
if cat_idx != -1:
    div_start = html.rfind('<div class="styles-module-root-boFHT', 0, cat_idx)
    div_end = html.find('>', div_start)
    div_tag = html[div_start:div_end+1]
    
    if 'id="avito-category-box"' not in div_tag:
        new_div_tag = div_tag[:-1] + ' id="avito-category-box" style="display: none;">'
        html = html[:div_start] + new_div_tag + html[div_end+1:]
        print("Added avito-category-box ID")

# 2. Add ID to the search box
# Followed by <div class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh ...">
search_idx = html.find('item_list_with_filters/search_input')
if search_idx != -1:
    div_start = html.rfind('<div class="styles-module-root-boFHT', 0, search_idx)
    div_end = html.find('>', div_start)
    div_tag = html[div_start:div_end+1]
    
    if 'id="avito-search-box"' not in div_tag:
        new_div_tag = div_tag[:-1] + ' id="avito-search-box" style="grid-column: span 4 / span 4;">'
        html = html[:div_start] + new_div_tag + html[div_end+1:]
        print("Added avito-search-box ID")

# 3. Add ID to custom-auto-filters and hide it by default
# It's already <div id="custom-auto-filters" ...>
# Let's ensure it has display: none by default
old_filters = '<div id="custom-auto-filters"'
new_filters = '<div id="custom-auto-filters" style="display: none;"'
# Actually wait, I already styled custom-auto-filters previously and maybe it has other styles.
# Let's use regex to safely add display: none if not present.
filters_idx = html.find('id="custom-auto-filters"')
if filters_idx != -1:
    tag_start = html.rfind('<div', 0, filters_idx)
    tag_end = html.find('>', filters_idx)
    tag = html[tag_start:tag_end+1]
    if 'display: none' not in tag:
        if 'style="' in tag:
            new_tag = tag.replace('style="', 'style="display: none; ')
        else:
            new_tag = tag[:-1] + ' style="display: none;">'
        html = html[:tag_start] + new_tag + html[tag_end+1:]
        print("Hid custom-auto-filters by default")

# 4. Update the Javascript logic
# Replace the JS inside the global click listener
js_old = """        var tabs = document.querySelector('.styles-module-root-fSK0J');"""
js_new = """        var tabs = document.querySelector('.styles-module-root-fSK0J');"""

# Wait, I need to completely replace the script we just wrote.
script_start = "<script>\ndocument.body.addEventListener('click', function(e) {"
idx_script = html.find(script_start)
if idx_script != -1:
    script_end = "});\n</script>\n</body>"
    idx_script_end = html.find(script_end, idx_script) + len(script_end)
    
    new_script = """<script>
document.body.addEventListener('click', function(e) {
    // Найти button
    var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
    if (searchBtn) {
        e.preventDefault();
        
        var tabs = document.querySelector('.styles-module-root-fSK0J');
        if(tabs) tabs.style.display = 'none';
        
        var searchHeader = document.getElementById('avito-search-header');
        if(searchHeader) searchHeader.style.display = 'block';
        
        var resultsBar = document.getElementById('results-count-bar');
        if(resultsBar) resultsBar.style.display = 'flex';
        
        var itemsGrid = document.querySelector('.ProfileItemsGrid-module-root-wq8JY');
        if(itemsGrid) itemsGrid.style.display = 'none';
        
        // Show Category Box and Shrink Search Box
        var catBox = document.getElementById('avito-category-box');
        if(catBox) catBox.style.display = 'block';
        
        var searchBox = document.getElementById('avito-search-box');
        if(searchBox) searchBox.style.gridColumn = 'span 3 / span 3';
        
        // Show Custom Filters
        var customFilters = document.getElementById('custom-auto-filters');
        if(customFilters) customFilters.style.display = 'block';
    }
    
    // < Профиль продавца button
    var backBtn = e.target.closest('#back-to-profile-btn');
    if (backBtn) {
        e.preventDefault();
        
        var tabs = document.querySelector('.styles-module-root-fSK0J');
        if(tabs) tabs.style.display = 'block';
        
        var searchHeader = document.getElementById('avito-search-header');
        if(searchHeader) searchHeader.style.display = 'none';
        
        var resultsBar = document.getElementById('results-count-bar');
        if(resultsBar) resultsBar.style.display = 'none';
        
        var itemsGrid = document.querySelector('.ProfileItemsGrid-module-root-wq8JY');
        if(itemsGrid) itemsGrid.style.display = 'block'; // Or block
        
        // Hide Category Box and Expand Search Box
        var catBox = document.getElementById('avito-category-box');
        if(catBox) catBox.style.display = 'none';
        
        var searchBox = document.getElementById('avito-search-box');
        if(searchBox) searchBox.style.gridColumn = 'span 4 / span 4';
        
        // Hide Custom Filters
        var customFilters = document.getElementById('custom-auto-filters');
        if(customFilters) customFilters.style.display = 'none';
    }
});
</script>
</body>"""
    
    html = html[:idx_script] + new_script + html[idx_script_end:]
    print("Updated JS logic.")

# Wait, there's another script that toggles the custom filters!
# Let's remove it because it interferes.
toggle_script = """<script>
(function() {
    window.addEventListener('click', function(e) {
        var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
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
        }
    }, true);
})();
</script>"""
if toggle_script in html:
    html = html.replace(toggle_script, "")
    print("Removed conflicting filter toggle script.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
