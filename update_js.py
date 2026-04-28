import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the old script block with the new event delegation script
old_script_start = '<script>\ndocument.addEventListener(\'DOMContentLoaded\', function() {'
old_script_end = '});\n</script>\n</body>'

idx_start = html.find(old_script_start)
if idx_start != -1:
    idx_end = html.find(old_script_end, idx_start) + len(old_script_end)
    
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
        if(itemsGrid) itemsGrid.style.display = 'block'; // Or whatever default is, usually block for Avito grids
    }
});
</script>
</body>"""

    html = html[:idx_start] + new_script + html[idx_end:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated JS to use event delegation.")
else:
    print("Old script not found")
