import sys

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('window.open(\'https://www.avito.ru/business\'')
idx2 = content.find('window.open(\'https://www.avito.ru/business\'', idx1 + 1)

print("First occurrence:")
print(content[max(0, idx1-100):idx1+200].encode('utf-8'))

print("\nSecond occurrence:")
print(content[max(0, idx2-100):idx2+200].encode('utf-8'))
