with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('https://i.ibb.co/68ZJ2F9/111.jpg', 'logo.jpg')

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated logo to use local logo.jpg")
