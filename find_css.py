import re
import json

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

links = re.findall(r'href="(https://[^\"]+\.css)"', html)
print(json.dumps(links, indent=2))
