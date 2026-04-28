import re

with open('js_template.js', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace comment photos block with ${commentPhotosHtml}
# We know it starts with <div class="styles-module-root-Ie3Kv" ...> and ends with </div></div></div>
template = re.sub(r'<div class="styles-module-root-Ie3Kv".*?</div></div></div>', '${commentPhotosHtml}', template, count=1, flags=re.DOTALL)

# But wait, the original HTML actually has <div class="styles-module-images-ycitL"> around it.
# Let's replace the whole <div class=""><div class="styles-module-images-ycitL">...</div></div></div></div> for BOTH!
template = re.sub(r'<div class=""><div class="styles-module-attributes-MWa1u">', '<div class="styles-module-attributes-MWa1u">', template, flags=re.DOTALL)
# Actually, let's just do a manual replacement to be extremely safe, since we know exactly what's inside js_template.js

# For comments, there is no images wrapper in the current js_template.js?
# Let's check: js_template.js line 1 ends right before the body.
# Let's just rewrite js_template.js from scratch using a clean template string!
