with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 10. Replace avatar backgrounds
            const allDivs = document.querySelectorAll('div, span');
            allDivs.forEach(div => {
                const bg = div.style.backgroundImage;
                if (bg && (bg.includes('gaztormoz') || bg.includes('54F-uLa4S2hIEYltPNug80IYSW7AGclgCBxJas4RQ2LI'))) {
                    div.style.backgroundImage = 'url("https://i.ibb.co/68ZJ2F9/111.jpg")';
                }
            });"""

if '// 10. Replace avatar backgrounds' not in text:
    text = text.replace("// 4. Update Native Gallery", js_addition + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Background replace logic")
else:
    print("Background replace logic already exists")
