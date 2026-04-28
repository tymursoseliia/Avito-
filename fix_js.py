import re

for filename in ['clean_avito (1).html', 'admin.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('const supabase = supabase.createClient', 'const supabaseClient = supabase.createClient')
    content = content.replace('await supabase.from', 'await supabaseClient.from')
    content = content.replace('await supabase.storage', 'await supabaseClient.storage')
    content = content.replace('supabase.storage.from', 'supabaseClient.storage.from')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print('Fixed JS in both files.')

