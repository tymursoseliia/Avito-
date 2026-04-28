import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject CSS
if 'dynamic-catalog-hide' not in content:
    content = content.replace('</head>', '<style id="dynamic-catalog-hide">.ProfileItemsGrid-module-root-wq8JY { opacity: 0; transition: opacity 0.3s ease-in; }</style></head>')

# 2. Add opacity = 1
# Let's just regex search for grid.innerHTML = activeCarsHtml;
content = re.sub(r'(grid\.innerHTML\s*=\s*activeCarsHtml;)', r'\1\n            grid.style.opacity = "1";', content)

# 3. Handle the active tab switch so we don't accidentally get hidden
content = re.sub(r'(tabActive\.onclick\s*=\s*\(\)\s*=>\s*\{.*?grid\.innerHTML\s*=\s*activeCarsHtml;)', r'\1\n            grid.style.opacity = "1";', content, flags=re.DOTALL)
content = re.sub(r'(tabClosed\.onclick\s*=\s*\(\)\s*=>\s*\{.*?grid\.innerHTML\s*=\s*completedCarsHtml;)', r'\1\n            grid.style.opacity = "1";', content, flags=re.DOTALL)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected opacity hide/show logic to prevent FOUC in clean_avito (1).html using robust regex")
