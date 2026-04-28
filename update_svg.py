import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_svg = """<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="transform: rotate(45deg); margin-bottom: 4px;">
                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path>
            </svg>"""

new_svg = """<svg role="img" aria-hidden="true" data-icon="my-location" viewBox="0 0 24 24" name="my-location" class="css-1bal07k" width="20" height="20" fill="currentColor" style="margin-right: 4px;">
                <path d="M2.649 10.939c-.86-.323-.867-1.536-.011-1.869l18-7c.81-.315 1.61.484 1.294 1.295l-7 18c-.333.856-1.546.848-1.868-.011l-2.84-7.575-7.575-2.84z"></path>
            </svg>"""

html = html.replace(old_svg, new_svg)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated region SVG icon.")
