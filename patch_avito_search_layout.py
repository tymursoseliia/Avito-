import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean up my previous incorrect insertions
html = re.sub(r'<div id="search-category-btn".*?</svg>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div id="search-category-btn-wrapper".*?</svg>\s*</span>\s*</label>\s*</div>', '', html, flags=re.DOTALL)

# 2. Insert the correct span_1 wrapper before the span_4 search wrapper
span_1_html = '''
<div class="styles-module-root-boFHT styles-module-root_span_1-mrCzn styles-module-root_compensation_none-fjYO3" id="search-category-btn-wrapper" style="display: none;">
  <label class="styles-module-root-xMJB7 styles-module-root_size-m-m1EB0" data-marker="item_list_with_filters/category_select" aria-disabled="false" tabindex="-1">
    <div class="styles-module-contentWrapper-H7tid">
      <div class="styles-module-content-mMdg8">
        <div class="styles-module-inputWrapper-ElVit styles-module-inputWrapper_fullWidth-vAlp5">
          <input marker="item_list_with_filters/category_select" aria-haspopup="true" aria-expanded="false" class="styles-module-input-VLI5k" data-marker="item_list_with_filters/category_select/input" value="Автомобили" readonly style="cursor: pointer; font-size: 14px;">
          <span class="styles-module-inputMirror-tflQY">Автомобили</span>
        </div>
      </div>
    </div>
    <span class="styles-module-icon-CkS9m styles-module-iconAfter-vRsvw">
      <svg role="img" aria-hidden="true" data-icon="category" viewBox="0 0 24 24" name="category" class="css-mbvo24">
        <path d="M19.4 9.7h-1.5c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45c-.11.21-.11.49-.11 1.05v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05v-1.5c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44c-.21-.11-.49-.11-1.05-.11ZM12.8 16.3h-1.5c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45c-.11.21-.11.49-.11 1.05v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05v-1.5c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44c-.21-.11-.49-.11-1.05-.11ZM12.8 9.7h-1.5c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45c-.11.21-.11.49-.11 1.05v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05v-1.5c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44c-.21-.11-.49-.11-1.05-.11ZM6.1 9.7H4.6c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45C3 10.46 3 10.74 3 11.3v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05v-1.5c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44c-.21-.11-.49-.11-1.05-.11ZM12.8 3h-1.5c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45c-.11.21-.11.49-.11 1.05v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05V4.6c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44C13.64 3 13.36 3 12.8 3ZM6.1 16.3H4.6c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45C3 17.06 3 17.34 3 17.9v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05v-1.5c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44C6.94 16.3 6.66 16.3 6.1 16.3Z"></path>
        <path d="M19.4 3h-1.5c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45c-.11.21-.11.49-.11 1.05v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05V4.6c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44C20.24 3 19.96 3 19.4 3ZM6.1 3H4.6c-.56 0-.84 0-1.05.1a1 1 0 0 0-.44.45C3 3.76 3 4.04 3 4.6v1.5c0 .56 0 .84.1 1.05a1 1 0 0 0 .45.44c.21.11.49.11 1.05.11h1.5c.56 0 .84 0 1.05-.1a1 1 0 0 0 .44-.45c.11-.21.11-.49.11-1.05V4.6c0-.56 0-.84-.1-1.05a1 1 0 0 0-.45-.44C6.94 3 6.66 3 6.1 3Z"></path>
      </svg>
    </span>
  </label>
</div>
'''

search_wrapper_match = re.search(r'(<div class="styles-module-root-boFHT styles-module-root_span_4-c4Vny[^>]*>\s*<div class="styles-module-root-jjade[^>]*>\s*<div class="styles-module-root-auHUM[^>]*>\s*<form data-marker="item_list_with_filters/query/form">)', html)
if search_wrapper_match:
    html = html.replace(search_wrapper_match.group(1), span_1_html + search_wrapper_match.group(1))
    print('Inserted span_1 correctly')
else:
    print('Could not find search wrapper')

# 3. Update the JS logic
old_js = """        var catBtn = document.getElementById('search-category-btn');
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

new_js = """        var catWrapper = document.getElementById('search-category-btn-wrapper');
        var filterMenu = document.getElementById('custom-auto-filters');
        
        // Find the tabs wrapper. It's the previous sibling element of the search wrapper generally.
        var tabsElement = document.querySelector('.styles-module-root-fSK0J');
        
        // Find the main search wrapper
        var searchForm = document.querySelector('[data-marker="item_list_with_filters/query/form"]');
        var searchWrapper = searchForm ? searchForm.closest('.styles-module-root-boFHT') : null;
        
        if (searchBtn || filterIcon) {
            e.preventDefault();
            e.stopPropagation();
            
            // Show new UI state
            if (tabsElement) tabsElement.style.display = 'none';
            if (customHeader) customHeader.style.display = 'block';
            if (catWrapper) catWrapper.style.display = 'block';
            if (filterMenu) filterMenu.style.display = 'block';
            
            if (searchWrapper) {
                searchWrapper.classList.remove('styles-module-root_span_4-c4Vny');
                searchWrapper.classList.add('styles-module-root_span_3-Fp6fh');
            }
        }
        
        if (backBtn) {
            e.preventDefault();
            e.stopPropagation();
            
            // Revert UI state
            if (tabsElement) tabsElement.style.display = 'block';
            if (customHeader) customHeader.style.display = 'none';
            if (catWrapper) catWrapper.style.display = 'none';
            if (filterMenu) filterMenu.style.display = 'none';
            
            if (searchWrapper) {
                searchWrapper.classList.remove('styles-module-root_span_3-Fp6fh');
                searchWrapper.classList.add('styles-module-root_span_4-c4Vny');
            }
        }"""

if old_js in html:
    html = html.replace(old_js, new_js)
    print("Updated JS successfully")
else:
    print("Could not find old JS")

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
