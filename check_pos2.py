with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<div class="ProfileItemsGrid-module-root-wq8JY"></div>')
print(html[pos-300:pos].encode('ascii', 'ignore').decode('ascii'))
