import json
import urllib.request
import urllib.parse
import re

url = "https://yjhjthhirxjxkbokycat.supabase.co/rest/v1/reviews"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg"

with open('extracted_reviews.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Clean up data
for r in reviews:
    if not r['date_text']:
        r['date_text'] = "Недавно"
    
    # Strip some known bad characters
    r['author_name'] = r['author_name'].strip()
    r['car_title'] = r['car_title'].strip()
    r['comment_text'] = r['comment_text'].replace('<br>', '\n').strip()
    r['reply_text'] = r['reply_text'].replace('<br>', '\n').replace('<br/>', '\n').strip()
    
    # Check if there is reply text. The old HTML had standard reply:
    if 'Автомиг' in r['reply_text'] or 'Уважаемый' in r['reply_text']:
        # Strip the HTML tags completely from reply text
        r['reply_text'] = re.sub(r'<[^>]+>', '', r['reply_text']).strip()

headers = {
    'apikey': key,
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

data = json.dumps(reviews).encode('utf-8')

req = urllib.request.Request(url, data=data, headers=headers, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(f"Successfully inserted {len(reviews)} reviews.")
except Exception as e:
    print(f"Failed: {e}")
    try:
        print(e.read().decode('utf-8'))
    except:
        pass
