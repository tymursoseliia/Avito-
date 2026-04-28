with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 3. Update Breadcrumbs
            const breadcrumbs = document.querySelectorAll('[data-marker="breadcrumbs"] a, [data-marker="breadcrumbs"] span');
            if (breadcrumbs.length >= 2) {
                const lastBreadcrumb = breadcrumbs[breadcrumbs.length - 1];
                if (lastBreadcrumb) {
                    lastBreadcrumb.textContent = car.title;
                }
            }"""

new_code = """            // 3. Update Breadcrumbs
            const breadcrumbItems = document.querySelectorAll('[data-marker="breadcrumbs"] span[itemprop="itemListElement"]');
            breadcrumbItems.forEach(item => {
                const text = item.textContent;
                if (text.includes('Zeekr') || text.includes('8X')) {
                    item.remove();
                }
            });
            
            // Also update the last breadcrumb to the car title
            const breadcrumbs = document.querySelectorAll('[data-marker="breadcrumbs"] a, [data-marker="breadcrumbs"] span');
            if (breadcrumbs.length >= 2) {
                const lastBreadcrumb = breadcrumbs[breadcrumbs.length - 1];
                if (lastBreadcrumb) {
                    lastBreadcrumb.textContent = car.title;
                }
            }"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated breadcrumb logic")
else:
    print("Could not find old breadcrumb logic")
