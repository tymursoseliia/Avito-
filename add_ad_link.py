with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
                if (a.textContent.includes('БАСТА') || a.textContent.includes('СИНЕРГИЯ') || a.textContent.includes('Школа музыки')) {
                    a.href = 'https://xn--80aac8afrzi0cyb.xn--p1ai/?aviclid=c4095ce4-7c11-44ca-ab0b-e6bcc84d98ab&marketer=zvv&produkt=393998515&utm_campaign=202604204&utm_gen=3&utm_medium=cpc&utm_source=avito-ads&utm_term=basta_s_textom_capitals';
                    a.target = '_blank';
                }
"""

text = text.replace("if (a.textContent.includes('#яПомогаю')) {", js_addition + "                if (a.textContent.includes('#яПомогаю')) {")

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated update_car_page.py with ad link")
