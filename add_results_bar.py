import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the end of custom-auto-filters. It ends with:
# <div id="more-filters-btn" ...>Меньше фильтров ...</div>
# </div>
# <div class="ProfileItemsGrid-module-root-wq8JY">

idx_grid = html.find('<div class="ProfileItemsGrid-module-root-wq8JY">')

if idx_grid != -1:
    results_bar = """
<div id="results-count-bar" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding: 0; font-family: 'Manrope', Arial, sans-serif;">
    <h2 style="font-size: 16px; font-weight: 800; margin: 0; color: #000;">Не найдено объявлений</h2>
    <div style="font-size: 14px; cursor: pointer; display: flex; align-items: center; gap: 4px; color: #000;">
        По умолчанию
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
            <path d="M16.293 9.293a1 1 0 0 1 1.414 1.414l-5 5a1 1 0 0 1-1.414 0l-5-5a1 1 0 0 1 1.414-1.414L12 13.586l4.293-4.293z"></path>
        </svg>
    </div>
</div>
"""
    # Let's see if results_bar is already there to avoid duplicates
    if 'id="results-count-bar"' not in html:
        html = html[:idx_grid] + results_bar + html[idx_grid:]
        
        # Also let's clear the grid so it really matches "Не найдено объявлений" 
        # Actually, let's keep the grid but hide it or remove it?
        # The user said "1в1 как тут", let's clear the items grid just to be safe, or just hide it.
        # I'll just clear the items grid to match "Не найдено".
        
        idx_grid_end = html.find('</div>', html.find('iva-item-root-Kcj9I', idx_grid))
        # It's safer to just empty the grid contents
        grid_start_tag = '<div class="ProfileItemsGrid-module-root-wq8JY">'
        grid_start_idx = html.find(grid_start_tag)
        # Find closing div of grid
        # The grid contains items. I'll just replace the grid entirely with an empty one.
        # Actually, it's easier to just use regex to replace everything inside the grid.
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully injected results-count-bar.")
    else:
        print("results-count-bar already exists.")
else:
    print("Could not find ProfileItemsGrid")
