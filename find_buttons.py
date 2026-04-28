import bs4
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('show_all_buttons.txt', 'w', encoding='utf-8') as out:
    for el in soup.find_all(string=lambda t: t and 'Показать' in t):
        parent = el.parent
        out.write(f"{parent.name} | class: {parent.get('class')} | id: {parent.get('id')} | text: {el.strip()}\n")
