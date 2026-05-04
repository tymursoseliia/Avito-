import os
import re
import requests

url = "https://yjhjthhirxjxkbokycat.supabase.co/rest/v1/company_photos?select=*&order=order_index.asc"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg"

headers = {
    "apikey": key,
    "Authorization": f"Bearer {key}"
}

def fetch_company_photos():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching photos: {response.text}")
        return []

def generate_photos_html(photos_data):
    if not photos_data:
        return ""
    
    html = ""
    for p in photos_data:
        photo_url = p.get("url")
        html += f'<img class="Gallery-module-image-rW4ZY" src="{photo_url}" style="width:208px; object-fit: cover; margin-right: 4px;" alt="Фото компании"/>'
    return html

def update_index_html():
    html_file = 'index.html'
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found.")
        return

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the container for the photos list
    start_marker = '<div class="Carousel-module-list-XIvtu" role="list">'
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Error: Could not find the photos container in index.html.")
        return

    inner_start_idx = start_idx + len(start_marker)
    end_idx = content.find('</div>', inner_start_idx)
    
    if end_idx == -1:
        print("Error: Could not find the end of photos container.")
        return

    print("Fetching photos from Supabase...")
    photos = fetch_company_photos()
    
    if not photos:
        print("No photos found in the database. HTML will not be modified.")
        return

    print(f"Fetched {len(photos)} photos. Generating HTML...")
    new_html = generate_photos_html(photos)

    # Replace old content
    updated_content = content[:inner_start_idx] + "\n" + new_html + "\n" + content[end_idx:]

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Successfully updated index.html with new company photos!")

if __name__ == "__main__":
    update_index_html()
