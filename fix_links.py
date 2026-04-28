import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# The links
link1 = 'href="https://www.avito.ru/business"'
new_link1 = 'href="https://www.avito.ru/business" target="_blank" onclick="window.open(\'https://www.avito.ru/business\', \'_blank\'); return false;"'

link2 = 'href="https://www.avito.ru/all/business360"'
new_link2 = 'href="https://www.avito.ru/all/business360" target="_blank" onclick="window.open(\'https://www.avito.ru/all/business360\', \'_blank\'); return false;"'

link3 = 'href="https://www.avito.ru/employer"'
new_link3 = 'href="https://www.avito.ru/employer" target="_blank" onclick="window.open(\'https://www.avito.ru/employer\', \'_blank\'); return false;"'

html = html.replace(link1, new_link1)
html = html.replace(link2, new_link2)
html = html.replace(link3, new_link3)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Links updated successfully")
