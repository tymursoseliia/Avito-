import sys
html = open('clean_avito (1).html', encoding='utf-8').read()
idx = html.find('id="custom-mega-dropdown"')
print(html[max(0, idx-150):idx+50].encode('utf-8'))
