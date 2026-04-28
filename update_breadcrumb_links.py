with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // Also update the last breadcrumb to the car title
            const breadcrumbs = document.querySelectorAll('[data-marker="breadcrumbs"] a, [data-marker="breadcrumbs"] span');
            if (breadcrumbs.length >= 2) {
                const lastBreadcrumb = breadcrumbs[breadcrumbs.length - 1];
                if (lastBreadcrumb) {
                    lastBreadcrumb.textContent = car.title;
                }
            }"""

new_code = """            // Also update the last breadcrumb to the car title
            const breadcrumbs = document.querySelectorAll('[data-marker="breadcrumbs"] a, [data-marker="breadcrumbs"] span');
            if (breadcrumbs.length >= 2) {
                const lastBreadcrumb = breadcrumbs[breadcrumbs.length - 1];
                if (lastBreadcrumb) {
                    lastBreadcrumb.textContent = car.title;
                }
            }
            
            // Redirect breadcrumb links to the main catalog
            const breadcrumbLinks = document.querySelectorAll('[data-marker="breadcrumbs"] a');
            breadcrumbLinks.forEach(link => {
                link.href = 'clean_avito (1).html';
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated breadcrumb link logic")
else:
    print("Could not find old breadcrumb logic")
