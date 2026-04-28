import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<div class="styles-module-root-fSK0J">'
idx_start = html.find(start_str)

# Find the end of this div. We know it ends with <div class="styles-module-underline-CxbUx"></div></div></div>
end_str = '<div class="styles-module-underline-CxbUx"></div></div></div>'
idx_end = html.find(end_str, idx_start)

if idx_start != -1 and idx_end != -1:
    idx_end += len(end_str)
    
    new_header = """
<div class="custom-avito-header" style="margin-bottom: 24px; font-family: 'Manrope', Arial, sans-serif;">
    <a href="#" style="text-decoration: none; color: #000; font-size: 14px; margin-bottom: 16px; display: inline-flex; align-items: center; gap: 4px;">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
            <path d="M15.293 3.293a1 1 0 0 1 1.414 1.414L8.414 12l8.293 8.293a1 1 0 0 1-1.414 1.414l-9-9a1 1 0 0 1 0-1.414l9-9z"></path>
        </svg>
        Профиль продавца
    </a>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1 style="font-size: 32px; font-weight: 800; margin: 0; letter-spacing: -0.5px;">Объявления</h1>
        <button type="button" style="display: flex; align-items: center; gap: 6px; background: none; border: none; font-size: 15px; font-weight: 500; cursor: pointer; padding: 0;">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="transform: rotate(45deg); margin-bottom: 4px;">
                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path>
            </svg>
            Все регионы
        </button>
    </div>
</div>
"""
    html = html[:idx_start] + new_header + html[idx_end:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully replaced tabs with new header.")
else:
    print("Could not find the target container.")
