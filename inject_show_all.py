with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

show_all_script = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const showAllButtons = Array.from(document.querySelectorAll('p, span, div, button')).filter(el => {
        const t = el.textContent.trim();
        return t === 'Показать все' || t === 'Показать' || t === 'Читать далее' || t === 'Показать ещё';
    });
    showAllButtons.forEach(btn => {
        btn.style.cursor = 'pointer';
        btn.onclick = (e) => {
            e.preventDefault();
            e.stopPropagation();
            let container = btn.parentElement.parentElement;
            if (container) {
                container.style.maxHeight = 'none';
                container.style.overflow = 'visible';
                const clamps = container.querySelectorAll('[class*="clamp"], [style*="-webkit-line-clamp"]');
                clamps.forEach(c => {
                    c.style.display = 'block';
                    c.style.webkitLineClamp = 'unset';
                });
                
                // If it's a review text
                const textContainer = btn.closest('div');
                if (textContainer) {
                    textContainer.style.maxHeight = 'none';
                    textContainer.style.webkitLineClamp = 'unset';
                    textContainer.style.display = 'block';
                }
                
                btn.style.display = 'none';
            }
        };
    });
});
</script>
"""

if "Показать все" in show_all_script and "showAllButtons" not in text:
    text = text.replace("</body>", show_all_script + "\n</body>")
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected show_all_script to clean_avito (1).html")

with open('update_car_page.py', 'r', encoding='utf-8') as f:
    up_text = f.read()

# Add the script to update_car_page.py as well so it gets added to car_page.html
if "showAllButtons" not in up_text:
    up_text = up_text.replace("const js_code = `", "const js_code = `" + show_all_script.replace("</script>", "").replace("<script>", ""))
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(up_text)
    print("Injected show_all_script to update_car_page.py")

