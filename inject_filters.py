import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject HTML before ProfileItemsGrid-module-root-wq8JY
filters_html = """
<div id="custom-auto-filters" class="custom-auto-filters-container" style="display: none; margin-bottom: 24px; padding: 0 10px;">
  <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 8px; margin-bottom: 8px;">
    <div class="custom-filter-select">
      <span class="custom-filter-text">Тип автомобиля</span>
      <span class="custom-filter-arrow">⌄</span>
    </div>
    <div class="custom-filter-input">
      <input type="text" placeholder="Цена от, ₽">
    </div>
    <div class="custom-filter-input">
      <input type="text" placeholder="Цена до, ₽">
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div class="custom-filter-select">
      <span class="custom-filter-text">Марка</span>
      <span class="custom-filter-arrow">⌄</span>
    </div>
    <div class="custom-filter-select">
      <span class="custom-filter-text">Модель</span>
      <span class="custom-filter-arrow">⌄</span>
    </div>
    <div class="custom-filter-select">
      <span class="custom-filter-text">Поколение</span>
      <span class="custom-filter-arrow">⌄</span>
    </div>
  </div>
  <div style="font-size: 14px; font-weight: 500; font-family: Manrope, sans-serif; cursor: pointer; color: #000;">
    Больше фильтров <span style="font-size: 12px; margin-left: 2px; color: #000;">⌄</span>
  </div>
</div>
"""

target_div = '<div class="ProfileItemsGrid-module-root-wq8JY">'
if target_div in html and 'id="custom-auto-filters"' not in html:
    html = html.replace(target_div, filters_html + '\n' + target_div)

# 2. Inject CSS
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
if 'custom-filter-select' not in html:
    html = html.replace('</head>', filters_css + '\n</head>')

# 3. Inject JS
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
if 'custom-auto-filters' in filters_html and 'getElementById(\'custom-auto-filters\')' not in html:
    html = html.replace('</body>', filters_js + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Filters menu injected.")
