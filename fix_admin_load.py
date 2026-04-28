import re

html_file = 'admin.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix switchTab
old_func = '''        function switchTab(tabId, el) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(tabId + '-tab').classList.add('active');
            el.classList.add('active');
        }'''

new_func = '''        function switchTab(tabId, el) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(tabId + '-tab').classList.add('active');
            el.classList.add('active');
            if (tabId === 'reviews') {
                loadAdminReviews();
            } else {
                loadAdminCars();
            }
        }'''

if old_func in html:
    html = html.replace(old_func, new_func)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed switchTab")
else:
    print("Could not find switchTab block exactly as expected.")

# Also, just in case, call loadAdminReviews() once on startup
if 'loadAdminCars();\n\n        function switchTab' in html:
    html = html.replace('loadAdminCars();\n\n        function switchTab', 'loadAdminCars();\n        loadAdminReviews();\n\n        function switchTab')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added initial loadAdminReviews()")

