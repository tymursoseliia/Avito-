import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all <span class="styles-module-counter-uAip7">65</span> or similar to 0 initially
new_text = re.sub(r'<span class="styles-module-counter-uAip7">\d+</span>', '<span class="styles-module-counter-uAip7">...</span>', text)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced static counters with ...")
