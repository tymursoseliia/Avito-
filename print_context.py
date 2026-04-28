html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="custom-auto-filters"')
print(html[max(0, idx-500):idx+200])
