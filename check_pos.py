with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<div id="custom-auto-filters"')
print(html[pos-300:pos+100].encode('ascii', 'ignore').decode('ascii'))
