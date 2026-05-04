import re
import json
import requests

url = "https://yjhjthhirxjxkbokycat.supabase.co/rest/v1/company_photos"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg"

headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def import_old_photos():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the container
    start_marker = '<div class="Carousel-module-list-XIvtu" role="list">'
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Could not find the photos container.")
        return

    end_idx = content.find('</div>', start_idx + len(start_marker))
    container_html = content[start_idx:end_idx]

    # Extract all src attributes from images in this container
    img_urls = re.findall(r'<img[^>]+src="([^"]+)"', container_html)
    
    if not img_urls:
        print("No images found to import.")
        return

    print(f"Found {len(img_urls)} images. Importing to Supabase...")

    # Delete all existing data
    requests.delete(f"{url}?id=not.eq.00000000-0000-0000-0000-000000000000", headers=headers)

    # Insert new data
    data_to_insert = []
    for i, img_url in enumerate(img_urls):
        data_to_insert.append({
            "url": img_url,
            "order_index": i * 10
        })

    # Bulk insert
    res = requests.post(url, headers=headers, json=data_to_insert)
    if res.status_code in [200, 201]:
        print("Successfully imported all photos into Supabase!")
    else:
        print(f"Failed to import photos: {res.text}")

if __name__ == "__main__":
    import_old_photos()
