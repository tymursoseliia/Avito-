with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<div class="tabs">')
if idx != -1:
    print(text[max(0, idx):min(len(text), idx+1000)])
