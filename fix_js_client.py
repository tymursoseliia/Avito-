import re

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace window.supabaseClient with supabaseClient
html = html.replace('await window.supabaseClient.from', 'await supabaseClient.from')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed supabaseClient reference")
