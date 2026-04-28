import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the bad CSS entirely
html = re.sub(
    r'\.completed-view \.photo-slider-image-PWbIy,.*?\}\n',
    '',
    html,
    flags=re.DOTALL
)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
