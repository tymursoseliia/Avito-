with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will remove the extra closing tags
old_str = "</a>\n</div></div></div>\n${badgeHtml}"
new_str = "</a>\n${badgeHtml}"

if old_str in text:
    text = text.replace(old_str, new_str)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed extra closing tags")
else:
    # Try another variation without newline
    old_str2 = "</a></div></div></div>\n${badgeHtml}"
    if old_str2 in text:
        text = text.replace(old_str2, "</a>\n${badgeHtml}")
        with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Fixed extra closing tags (no newline)")
    else:
        print("Extra closing tags not found")
