with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'<div class="tab" onclick="switchTab\(\'company\', this\)">Настройки компании</div>', '', text)

# Also ensure tab-company content is removed
text = re.sub(r'<div id="company-tab" class="tab-content">.*?</form>\s*</div>', '', text, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Removed Настройки компании from admin.html')
