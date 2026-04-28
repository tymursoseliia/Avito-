with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "${r.comment_text.substring(0, 100)}",
    "${(r.comment_text || '').substring(0, 100)}"
)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
