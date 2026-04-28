import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# We know the block starts with:
# <script>
# document.addEventListener('DOMContentLoaded', function() {
#     setTimeout(function() {
#         var dropdownHTML = `
#         <div id="custom-mega-dropdown" class="custom-mega-dropdown">

pattern = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*setTimeout\(function\(\) \{\s*var dropdownHTML = `.*?</div>\s*`;\s*var div = document\.createElement.*?\}\);\s*\}, 1500\);\s*\}\);\s*</script>'

# Find all matches
matches = list(re.finditer(pattern, text, flags=re.DOTALL))
print("Found", len(matches), "matches.")

if len(matches) > 1:
    # Keep only the last one
    # Replace all with empty, then append the last one?
    # Actually, let's just replace the first one with empty.
    for match in matches[:-1]:
        start = match.start()
        end = match.end()
        text = text[:start] + text[end:]
    
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Duplicates removed.')
else:
    print('No duplicates found.')

