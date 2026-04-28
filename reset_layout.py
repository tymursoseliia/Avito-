import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore avito-category-box to visible
cat_box_old = 'id="avito-category-box" style="display: none;"'
cat_box_new = 'id="avito-category-box"'
html = html.replace(cat_box_old, cat_box_new)

# 2. Restore avito-search-box to its normal state without width hacks
search_box_old = 'id="avito-search-box" class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3" style="flex: 0 0 100% !important; max-width: 100% !important; grid-column: span 4 / span 4 !important;"'
search_box_new = 'id="avito-search-box" class="styles-module-root-boFHT styles-module-root_span_3-Fp6fh styles-module-root_compensation_none-fjYO3"'
html = html.replace(search_box_old, search_box_new)

# 3. Update the JS logic
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
        
        var customFilters = document.getElementById('custom-auto-filters');
        if(customFilters) customFilters.style.display = 'block';
    }
    
    // < Профиль продавца button
    var backBtn = e.target.closest('#back-to-profile-btn');
    if (backBtn) {
        e.preventDefault();
        window.location.reload(); // Simple and perfectly restores the original state!
    }
});
</script>
</body>"""
    
    html = html[:idx_script] + new_script + html[idx_script_end:]
    print("Cleaned up grid hacks and updated back button to use reload.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
