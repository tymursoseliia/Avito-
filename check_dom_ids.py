with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = ['add-car-form', 'submit-btn', 'toast', 'images', 'file-list', 'cars-list']
for dom_id in ids:
    if f'id="{dom_id}"' not in html:
        print(f'MISSING: {dom_id}')
else:
    print('All IDs found.')
