with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<div class="tabs">')
if idx != -1:
    with open('tabs_output.txt', 'w', encoding='utf-8') as out:
        out.write(text[max(0, idx):min(len(text), idx+2000)])
