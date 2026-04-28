import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace GAZTORMOZ case-insensitively with Автомиг
# We might want to replace "GAZTORMOZ" -> "АВТОМИГ" if it's all caps, 
# but the user asked for "Автомиг". Let's do a simple case-insensitive replacement.
# But wait, what if it's part of a URL or image path? 
# "gaztormoz" in image paths shouldn't be replaced if they break!
# Let's check if it exists in any URLs.
