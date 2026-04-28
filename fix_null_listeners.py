with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix company-logo addEventListener
html = html.replace(
    "document.getElementById('company-logo').addEventListener",
    "document.getElementById('company-logo')?.addEventListener"
)
html = html.replace(
    "document.getElementById('company-about-photos').addEventListener",
    "document.getElementById('company-about-photos')?.addEventListener"
)

# Fix companyForm addEventListener
old_company_form = """        const companyForm = document.getElementById('company-form');
        const companySubmitBtn = document.getElementById('company-submit-btn');

        companyForm.addEventListener('submit', async (e) => {"""
new_company_form = """        const companyForm = document.getElementById('company-form');
        const companySubmitBtn = document.getElementById('company-submit-btn');

        companyForm?.addEventListener('submit', async (e) => {"""
html = html.replace(old_company_form, new_company_form)

# And for reviewForm? It exists, but let's be safe:
html = html.replace("reviewForm.addEventListener", "reviewForm?.addEventListener")
html = html.replace("form.addEventListener", "form?.addEventListener")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
