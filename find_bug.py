import sys

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('target="_blank" onclick')
if idx != -1:
    print(content[max(0, idx-150):idx+250].encode('utf-8'))
else:
    print("Not found")
