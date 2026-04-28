import sys
import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the ID assignment with inline onclick
old_tag_start = '<a id="btn-more-dropdown" role="button"'
new_tag_start = '<a id="btn-more-dropdown" onclick="document.getElementById(\'custom-mega-dropdown\').classList.toggle(\'show\'); event.preventDefault(); event.stopPropagation(); return false;" role="button"'

if old_tag_start in html:
    html = html.replace(old_tag_start, new_tag_start)
    print("Replaced with inline onclick.")
else:
    print("Could not find old tag.")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done.")
