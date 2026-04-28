import re
with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

limit = text.find('<!-- Supabase JS -->')
if limit != -1: text = text[:limit]

# Find ALL li elements that contain an image
matches = re.findall(r'(<li[^>]*>.*?<img[^>]*>.*?</li>)', text, flags=re.DOTALL)
print('Found li with img:', len(matches))

if len(matches) > 0:
    print('First match:', matches[0][:200])
