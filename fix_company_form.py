with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "document.getElementById('company-form').addEventListener",
    "document.getElementById('company-form')?.addEventListener"
)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
