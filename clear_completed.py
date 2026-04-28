import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the giant string assigned to completedCarsHtml
content = re.sub(r'let completedCarsHtml = ".*?";', 'let completedCarsHtml = \'<p style="padding: 20px; font-family: Manrope, sans-serif; font-size: 16px;">Нет объявлений.</p>\';', content, flags=re.DOTALL)

# Update the completed tab counter
content = re.sub(r'completedTabCounter\.innerText\s*=\s*".*?";', 'completedTabCounter.innerText = "0";', content)
content = re.sub(r'completedTabCounter\.innerText\s*=\s*\d+;', 'completedTabCounter.innerText = "0";', content)

# Check if there is a place where we do `completedTabCounter.innerText = dbCompletedCount + 12;`
content = re.sub(r'completedTabCounter\.innerText\s*=\s*dbCompletedCount.*?;', 'completedTabCounter.innerText = "0";', content)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Completed cars cleared.")
