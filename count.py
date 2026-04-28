import sys

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Count 1:", content.count('window.open(\'https://www.avito.ru/business\''))
print("Count 2:", content.count('window.open(\'https://www.avito.ru/all/business360\''))
print("Count 3:", content.count('window.open(\'https://www.avito.ru/employer\''))
