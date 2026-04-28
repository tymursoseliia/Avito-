import os
import re
import urllib.request
import time

html_file = 'clean_avito (1).html'
css_dir = 'css'

if not os.path.exists(css_dir):
    os.makedirs(css_dir)

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

links = set(re.findall(r'href="(https://[^\"]+\.css)"', html))
print(f"Found {len(links)} unique CSS links to download.")

for url in links:
    filename = url.split('/')[-1]
    local_path = os.path.join(css_dir, filename)
    
    print(f"Downloading {url} -> {local_path}")
    
    # Try downloading the CSS file
    try:
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response:
            css_content = response.read()
            with open(local_path, 'wb') as f:
                f.write(css_content)
        
        # Replace the URL in the HTML with the local path
        local_url = f"./css/{filename}"
        html = html.replace(url, local_url)
        print(f"Successfully downloaded and replaced {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
    
    time.sleep(0.5)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done updating CSS links!")
