import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script [^>]*src=[\'"]([^\'"]+\.js)[\'"]', text)
print("JS scripts found:", scripts)

# Let's also find all links to avito.st
avito_st_scripts = re.findall(r'<script [^>]*src=[\'"](https://www.avito.st[^\'"]+)[\'"]', text)
print("Avito ST scripts found:", len(avito_st_scripts))
for s in avito_st_scripts:
    print(s)
