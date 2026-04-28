with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 1020 and line.strip() == '}':
        # Skip this rogue brace
        continue
    new_lines.append(line)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Removed rogue brace from admin.html")
