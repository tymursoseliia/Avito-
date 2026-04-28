with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix DOMContentLoaded issue
old_init = "if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', loadCars); } else { loadCompanyProfile();\n            loadCars(); }"
new_init = "if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', () => { loadCompanyProfile(); loadCars(); }); } else { loadCompanyProfile(); loadCars(); }"

if old_init in text:
    text = text.replace(old_init, new_init)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed loadCompanyProfile init in clean_avito (1).html")
else:
    print("Could not find init logic in clean_avito")

# Now check update_car_page.py regex
with open('update_car_page.py', 'r', encoding='utf-8') as f:
    up_text = f.read()

# I used replace(/\\n/g, '<br>') which becomes replace(/\n/g, '<br>')
# I need to use replace(/\\\\n/g, '<br>') so it writes /\\n/g
if "replace(/\\n/g, '<br>')" in up_text:
    up_text = up_text.replace("replace(/\\n/g, '<br>')", "replace(/\\\\n/g, '<br>')")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(up_text)
    print("Fixed regex in update_car_page.py")
else:
    print("Could not find regex in update_car_page.py")

