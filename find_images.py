import re
with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

limit = text.find('<!-- Supabase JS -->')
if limit != -1: text = text[:limit]

matches = re.findall(r'<img[^>]*src="([^"]*\.jpg)"[^>]*>', text)
print('Images found:', len(matches))
if len(matches) > 0:
    for m in matches[:5]:
        print(m)
        
# also check if there is a class "photo-slider" or something
if "photo-slider" in text:
    print("Found photo-slider class!")
