import re

with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the exact tab div by finding the substring index
idx = text.find('onclick="switchTab(\'company\'')
if idx != -1:
    start_idx = text.rfind('<div', 0, idx)
    end_idx = text.find('</div>', idx) + 6
    text = text[:start_idx] + text[end_idx:]

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Tab removed completely')
