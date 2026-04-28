with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

old_arrow = '<span class="custom-filter-arrow">⌄</span>'
new_arrow = '''<span class="custom-filter-arrow" style="display: flex; align-items: center;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 16px; height: 16px;">
            <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </span>'''

if old_arrow in html:
    html = html.replace(old_arrow, new_arrow)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced all arrows.")
else:
    print("Old arrow not found.")
