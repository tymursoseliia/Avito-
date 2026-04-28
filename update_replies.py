import urllib.request
import json
import random

url = 'https://yjhjthhirxjxkbokycat.supabase.co/rest/v1/reviews'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg'

replies = [
    "Спасибо за ваш отзыв! Рады, что вы остались довольны покупкой. Ждем вас снова!",
    "Благодарим за высокую оценку! Приятного пользования автомобилем!",
    "Спасибо за доверие! Наша команда всегда готова помочь вам. Удачи на дорогах!",
    "Отличный выбор! Спасибо, что выбрали наш автосалон. Желаем ровных дорог!",
    "Благодарим за приятные слова! Стараемся для вас. Обращайтесь, если будут вопросы!",
    "Спасибо за ваш комментарий! Очень рады, что смогли подобрать идеальный автомобиль для вас.",
    "Признательны за ваш отзыв! Пусть новый автомобиль приносит только радость!",
    "Спасибо, что нашли время поделиться впечатлениями. Рады были помочь!",
    "Благодарим за отзыв! Всегда рады видеть вас в нашем автосалоне!",
    "Спасибо за отличную оценку нашей работы. Будем рады дальнейшему сотрудничеству!"
]

# Fetch all reviews
req = urllib.request.Request(url + '?select=*', headers={'apikey': key, 'Authorization': 'Bearer ' + key})
response = urllib.request.urlopen(req)
reviews = json.loads(response.read().decode('utf-8'))

updated_count = 0

for r in reviews:
    # We will update ANY review that already had a reply, to make it shorter and random
    if r.get('reply_text') and len(r.get('reply_text')) > 0:
        new_reply = random.choice(replies)
        
        # Update in supabase
        update_url = f"{url}?id=eq.{r['id']}"
        data = json.dumps({'reply_text': new_reply}).encode('utf-8')
        
        patch_req = urllib.request.Request(update_url, data=data, headers={
            'apikey': key, 
            'Authorization': 'Bearer ' + key,
            'Content-Type': 'application/json',
            'Prefer': 'return=minimal'
        }, method='PATCH')
        
        urllib.request.urlopen(patch_req)
        updated_count += 1

print(f"Successfully updated {updated_count} reviews with random short replies.")
