with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix submit logic
old_submit = "price: parseInt(document.getElementById('price').value),"
new_submit = "price: parseInt(document.getElementById('price').value),\n                    description: document.getElementById('description').value,"

text = text.replace(old_submit, new_submit)

# Fix edit logic
old_edit = "document.getElementById('price').value = car.price;"
new_edit = "document.getElementById('price').value = car.price;\n            document.getElementById('description').value = car.description || '';"

text = text.replace(old_edit, new_edit)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed admin logic")
