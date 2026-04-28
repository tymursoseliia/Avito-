import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

start_tag = '<div id="custom-auto-filters"'
end_tag = '<div class="ProfileItemsGrid-module-root-wq8JY"></div>'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

if start_idx != -1 and end_idx != -1:
    filters_html = html[start_idx:end_idx]
    
    # Remove it from the current position
    html = html[:start_idx] + html[end_idx:]
    
    # Find the search button
    search_btn_str = '<button class="styles-module-root-wdGw5 styles-module-root_size_m-jsWyU styles-module-root_preset_primary-YvYPW styles-module-root_fullWidth-TCOfE"'
    
    btn_pos = html.find(search_btn_str)
    if btn_pos != -1:
        # We need to find the closing div of styles-module-root-xEbQv
        # Let's count 5 </div> tags after the button to reach the end of styles-module-root-xEbQv
        pos = btn_pos
        for _ in range(5):
            pos = html.find('</div>', pos) + 6
            
        html = html[:pos] + '\n' + filters_html + html[pos:]
        print('Moved custom-auto-filters block successfully')
        
        with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
            f.write(html)
    else:
        print('Search button not found')
else:
    print('Start or end tag not found')
