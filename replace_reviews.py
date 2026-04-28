import json
import urllib.request
import urllib.parse
import re

url = "https://yjhjthhirxjxkbokycat.supabase.co/rest/v1/reviews"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg"

headers = {
    'apikey': key,
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# 1. DELETE ALL REVIEWS
delete_url = url + "?id=not.is.null"
req_del = urllib.request.Request(delete_url, headers=headers, method='DELETE')
try:
    with urllib.request.urlopen(req_del) as response:
        print("Deleted old reviews.")
except Exception as e:
    print(f"Delete failed: {e}")

# 2. INSERT NEW REVIEWS
with open('extracted_reviews.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

for r in reviews:
    if not r['date_text']:
        r['date_text'] = "Недавно"

data = json.dumps(reviews).encode('utf-8')
req_ins = urllib.request.Request(url, data=data, headers=headers, method='POST')

try:
    with urllib.request.urlopen(req_ins) as response:
        res = response.read()
        print(f"Successfully inserted {len(reviews)} correct reviews with replies.")
except Exception as e:
    print(f"Insert failed: {e}")
    try:
        print(e.read().decode('utf-8'))
    except:
        pass
