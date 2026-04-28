import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore the filter toggle logic to trigger on searchBtn again
old_filter_js = """        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        
        if (filterIcon) {"""
new_filter_js = """        var searchBtn = e.target.closest('[data-marker="item_list_with_filters/search_button"]');
        var filterIcon = e.target.closest('[data-marker="item_list_with_filters/query/filters_icon"]');
        
        if (searchBtn || filterIcon) {"""
html = html.replace(old_filter_js, new_filter_js)

# 2. Restore the mega dropdown logic to ONLY trigger on 'Ещё'
old_mega_js = """            while (target && target !== document.body) {
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
new_mega_js = """            while (target && target !== document.body) {
                if (target.textContent && target.textContent.trim().startsWith('Ещё') && target.tagName === 'A') {
                    isMoreBtn = true;
                    btnElement = target;
                    break;
                }
                target = target.parentNode;
            }"""
html = html.replace(old_mega_js, new_mega_js)

# 3. Restore the padding of custom-auto-filters
html = html.replace('style="display: none; margin-bottom: 24px; padding: 0;"', 'style="display: none; margin-bottom: 24px; padding: 0 10px;"')

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Reverted naiti fix and restored padding")
