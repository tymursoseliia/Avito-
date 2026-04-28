import re
with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

# Find the <a> tag that contains the text 'БАСТА'
matches = re.findall(r'(<a[^>]*>.*?БАСТА.*?</a>)', text, flags=re.DOTALL | re.IGNORECASE)
if len(matches) > 0:
    with open('ad_debug.txt', 'w', encoding='utf-8') as f:
        f.write(matches[0][:500])
    print('Ad written')
else:
    print('Ad not found in <a> tag')
