import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the logo URL
old_logo = 'https://70.img.avito.st/image/1/1.ogFkvLa5GOhSG4zuLN6wOkoeDO7WOYzu0hUu6tIfGOo.DD1WHCne7V9xcT0-BplTPVR-nMNUotlxjG7IidMeKtQ'
new_logo = './logo.jpg'

html = html.replace(old_logo, new_logo)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo replaced.")
