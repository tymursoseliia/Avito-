import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the logo URL
old_logo = 'https://40.img.avito.st/image/1/1.k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk'
new_logo = './logo.jpg'

html = html.replace(old_logo, new_logo)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo replaced.")
