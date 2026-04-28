with open('admin.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find("form.addEventListener('submit'")
if idx == -1: idx = text.find('form.addEventListener("submit"')

if idx != -1:
    print(text[max(0, idx-50):min(len(text), idx+1000)])
else:
    print("Not found")
