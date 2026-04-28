import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove any existing search-category-btn
html = re.sub(r'<div id="search-category-btn".*?</svg>\s*</div>', '', html, flags=re.DOTALL)

# Re-insert it at the correct location
cat_btn_html = '''
<div id="search-category-btn" style="display: none; background: #f2f2f2; border-radius: 8px; padding: 0 16px; height: 48px; align-items: center; gap: 8px; cursor: pointer; margin-right: 8px; flex-shrink: 0;">
  <span style="font-size: 14px; font-family: Manrope, sans-serif;">Автомобили</span>
  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4 4h4v4H4V4zm6 0h4v4h-4V4zm6 0h4v4h-4V4zM4 10h4v4H4v-4zm6 0h4v4h-4v-4zm6 0h4v4h-4v-4zM4 16h4v4H4v-4zm6 0h4v4h-4v-4zm6 0h4v4h-4v-4z"/></svg>
</div>
'''

# Find the form and its parent div
match = re.search(r'(<div class="styles-module-root-auHUM[^>]*>\s*<form data-marker="item_list_with_filters/query/form">)', html)
if match:
    html = html.replace(match.group(1), cat_btn_html + match.group(1))
    print('Inserted at correct location')
else:
    print('Could not find form')

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
