import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the correct CSS for the completed view
correct_css = """
<style>
.completed-view [data-marker="item-photo"] {
    opacity: 0.5;
    filter: grayscale(100%);
}
</style>
"""

# We'll put it right before </head>
html = html.replace('</head>', correct_css + '\n</head>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Correct CSS injected.")
