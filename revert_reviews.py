import re

# Read the HTML file
html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to remove the entire <script>...</script> block that contains `// --- DYNAMIC REVIEWS SCRIPT ---`
js_start = html.find('// --- DYNAMIC REVIEWS SCRIPT ---')
if js_start != -1:
    script_start = html.rfind('<script>', 0, js_start)
    script_end = html.find('</script>', js_start) + 9
    
    # Remove the script block
    final_html = html[:script_start] + html[script_end:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Reverted to static comments!")
else:
    print("Could not find dynamic JS block")
