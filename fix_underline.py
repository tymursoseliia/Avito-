import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the underline for the active tab
# The class styles-module-underline-CxbUx needs inline width and transform because React isn't running to set them.
old_underline = '<div class="styles-module-underline-CxbUx"></div>'
# 132px is an estimated width for "Активные 65"
new_underline = '<div class="styles-module-underline-CxbUx" style="width: 132px; transform: translateX(0px);"></div>'

html = html.replace(old_underline, new_underline)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Added inline style to the tab underline element.")
