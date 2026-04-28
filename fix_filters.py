import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

filters_css = """
<style>
.custom-filter-select, .custom-filter-input {
    background-color: #F2F2F2;
    border-radius: 8px;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0 12px;
    box-sizing: border-box;
    cursor: pointer;
}
.custom-filter-select {
    justify-content: space-between;
}
.custom-filter-text {
    color: #8f8f8f;
    font-size: 14px;
    font-family: Manrope, sans-serif;
}
.custom-filter-arrow {
    color: #8f8f8f;
    font-size: 16px;
}
.custom-filter-input input {
    border: none;
    background: transparent;
    width: 100%;
    outline: none;
    font-size: 14px;
    font-family: Manrope, sans-serif;
    color: #000;
}
.custom-filter-input input::placeholder {
    color: #8f8f8f;
}
</style>
"""

filters_js = """
<script>
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
</script>
"""

if 'custom-filter-select {' not in html:
    html = html.replace('</head>', filters_css + '\n</head>')

if 'getElementById(\'custom-auto-filters\')' not in html:
    html = html.replace('</body>', filters_js + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS and JS fixed.")
