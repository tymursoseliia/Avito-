with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'<div class="tab" onclick="switchTab\(\'company\', this\)">Настройки компании</div>', '', text)
text = re.sub(r'<div id="tab-company" class="tab-content">.*?</form>\s*</div>', '', text, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done')
