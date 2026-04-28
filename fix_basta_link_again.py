with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 8. Fix Basta Ad Link
            const allElements = document.querySelectorAll('*');
            allElements.forEach(el => {
                if (el.children.length === 0 && el.textContent && (el.textContent.includes('БАСТА') || el.textContent.includes('СИНЕРГИЯ'))) {
                    // Find the container roughly 5 levels up to capture the whole ad block
                    let container = el;
                    for (let i = 0; i < 5; i++) {
                        if (container.parentElement) container = container.parentElement;
                    }
                    container.style.cursor = 'pointer';
                    container.onclick = function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        window.open('https://xn--80aac8afrzi0cyb.xn--p1ai/?aviclid=c4095ce4-7c11-44ca-ab0b-e6bcc84d98ab&marketer=zvv&produkt=393998515&utm_campaign=202604204&utm_gen=3&utm_medium=cpc&utm_source=avito-ads&utm_term=basta_s_textom_capitals', '_blank');
                    };
                }
            });"""

new_code = """            // 8. Fix Basta Ad Link
            const adTitles = document.querySelectorAll('strong');
            adTitles.forEach(el => {
                if (el.textContent && (el.textContent.includes('БАСТА') || el.textContent.includes('СИНЕРГИЯ'))) {
                    // Find the closest ad container (go up ~4 levels)
                    let container = el;
                    for (let i = 0; i < 4; i++) {
                        if (container.parentElement && container.parentElement.tagName !== 'BODY') {
                            container = container.parentElement;
                        }
                    }
                    
                    // Make the container clickable
                    container.style.cursor = 'pointer';
                    container.onclick = function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        window.open('https://xn--80aac8afrzi0cyb.xn--p1ai/?aviclid=c4095ce4-7c11-44ca-ab0b-e6bcc84d98ab&marketer=zvv&produkt=393998515&utm_campaign=202604204&utm_gen=3&utm_medium=cpc&utm_source=avito-ads&utm_term=basta_s_textom_capitals', '_blank');
                    };
                }
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed robust Basta ad link logic")
else:
    print("Basta ad logic not found")
