import re

# 1. Revert admin.html
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_text = f.read()

# Remove tab button
admin_text = re.sub(r'<button class="tab-button" onclick="switchAdminTab\(\'company\'\)">Настройки компании</button>', '', admin_text)

# Remove tab content
admin_text = re.sub(r'<div id="tab-company" class="tab-content">.*?</form>\s*</div>', '', admin_text, flags=re.DOTALL)

# Remove company profile logic
admin_text = re.sub(r'// --- COMPANY PROFILE LOGIC ---.*?}\);', '', admin_text, flags=re.DOTALL)

# Remove loadCompanyProfile() call
admin_text = admin_text.replace('loadCompanyProfile();\n', '')
admin_text = admin_text.replace('loadCompanyProfile();', '')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_text)

# 2. Revert clean_avito (1).html
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    clean_text = f.read()

# Remove loadCompanyProfile function entirely
clean_text = re.sub(r'async function loadCompanyProfile\(\)\s*\{.*?}\s*catch\(e\)\s*\{\s*console\.error\(\'Error in loadCompanyProfile:\',\s*e\);\s*}\s*}', '', clean_text, flags=re.DOTALL)

# Revert DOMContentLoaded logic
clean_text = clean_text.replace(
    "if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', () => { loadCompanyProfile(); loadCars(); }); } else { loadCompanyProfile(); loadCars(); }",
    "if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', loadCars); } else { loadCars(); }"
)

# Remove injected show_all_script
show_all_regex = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*\(\)\s*=>\s*\{\s*const showAllButtons.*?</script>'
clean_text = re.sub(show_all_regex, '', clean_text, flags=re.DOTALL)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(clean_text)


# 3. Revert update_car_page.py
with open('update_car_page.py', 'r', encoding='utf-8') as f:
    up_text = f.read()

# Remove loadCompanyProfile function from js_code
up_text = re.sub(r'async function loadCompanyProfile\(\)\s*\{.*?\}\s*loadCompanyProfile\(\);\s*', '', up_text, flags=re.DOTALL)

# Remove showAllButtons from update_car_page.py
up_text = re.sub(r'document\.addEventListener\(\'DOMContentLoaded\',\s*\(\)\s*=>\s*\{\s*const showAllButtons.*?\n\}\);\n', '', up_text, flags=re.DOTALL)

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(up_text)

print("Rollback complete.")
