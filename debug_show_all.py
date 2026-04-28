import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Показать все')

# Let's find the parent container of the "Показать все" button
# And also where the hidden items are.
# Let's search for the ID or class that hides them.
# The user wants "Показать все" to expand the hidden items.
# Usually it's a div with `data-marker="trust-factors/show-more"`.

# Let's print a larger context around the button without decoding issues.
# We'll save it to a file.
with open('debug_show_all.txt', 'w', encoding='utf-8') as out:
    out.write(html[max(0, idx-1000):min(len(html), idx+2000)])

print("Wrote to debug_show_all.txt")
