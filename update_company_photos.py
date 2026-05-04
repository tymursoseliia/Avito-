import os
import re
from supabase import create_client, Client

# Supabase setup
url: str = "https://yjhjthhirxjxkbokycat.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg"
supabase: Client = create_client(url, key)

def fetch_company_photos():
    response = supabase.table("company_photos").select("*").order("order_index").execute()
    return response.data

def generate_photos_html(photos_data):
    if not photos_data:
        return ""
    
    html = ""
    for p in photos_data:
        url = p.get("url")
        # You can adjust the width if you prefer
        html += f'<img class="Gallery-module-image-rW4ZY" src="{url}" style="width:208px; object-fit: cover; margin-right: 4px;" alt="Фото компании"/>'
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
    end_marker = '</div>'

    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Error: Could not find the photos container in index.html.")
        return

    # We need to find the closing div of the Carousel-module-list
    # Since it might have nested elements, we just find the next </div>
    # Actually, the original HTML just has <img> tags inside.
    # So the next </div> is the end of the container.
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
    try:
        import supabase
    except ImportError:
        print("Installing supabase-py...")
        os.system("pip install supabase")
    
    update_index_html()
