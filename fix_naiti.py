import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the filter toggle logic to NOT trigger on searchBtn
old_filter_js = """        var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        
        if (searchBtn || filterIcon) {"""
new_filter_js = """        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        
        if (filterIcon) {"""
html = html.replace(old_filter_js, new_filter_js)

# 2. Update the mega dropdown logic to ALSO trigger on 'Найти' and the search input
old_mega_js = """            while (target && target !== document.body) {
                if (target.textContent && target.textContent.trim().startsWith('Ещё') && target.tagName === 'A') {
                    isMoreBtn = true;
                    btnElement = target;
                    break;
                }
                target = target.parentNode;
            }"""
new_mega_js = """            while (target && target !== document.body) {
                if (target.textContent && target.textContent.trim().startsWith('Ещё') && target.tagName === 'A') {
                    isMoreBtn = true;
                    btnElement = target;
                    break;
                }
                var searchBtn = target.closest && target.closest('[data-marker="item_list_with_filters/search_button"]');
                var searchInput = target.closest && target.closest('[data-marker="item_list_with_filters/query/query/input"]');
                
                if (searchBtn || searchInput) {
                    isMoreBtn = true; // reusing the same flag for convenience
                    btnElement = searchBtn || searchInput;
                    break;
                }
                target = target.parentNode;
            }"""
html = html.replace(old_mega_js, new_mega_js)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated click handlers")
