import re

with open('js_template.js', 'r', encoding='utf-8') as f:
    template_str = f.read()

template_str = re.sub(r'<div class=""><div class="styles-module-images-ycitL">.*?</div></div></div></div>', '${replyPhotosHtml}', template_str)
template_str = template_str.replace('<div class="styles-module-text-sections-tKN7j">', '${commentPhotosHtml}<div class="styles-module-text-sections-tKN7j">')

print('${commentPhotosHtml}' in template_str)
print('${replyPhotosHtml}' in template_str)
