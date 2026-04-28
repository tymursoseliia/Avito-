import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

links = re.findall(r'<a[^>]*?href=\"(https://(vk\.com|ok\.ru|t\.me|www\.youtube\.com|rutube\.ru)[^\"]*)\"[^>]*>', html, flags=re.IGNORECASE)
print(f"Found {len(links)} social links matching.")
for l in links:
    print(l[0])
