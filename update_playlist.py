import requests
import json

# Source URL jahan se hume latest live events data fetch karna hai
SOURCE_URL = "https://raw.githubusercontent.com/drmlive/sliv-live-events/main/sonyliv.json"

def fetch_and_update():
    try:
        # Source se raw data fetch karein
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            data = response.json()
            
            # JSON file ko apni repository ke liye local save karein
            with open("sonyliv.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print("Successfully updated sonyliv.json!")
            
            # (Optional) Agar aap .m3u8 playlist bhi banana chahte hain, to is code ko use kar sakte hain:
            # generate_m3u(data)
            
        else:
            print(f"Failed to fetch data, Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# (Optional) M3U Playlist generator function
def generate_m3u(data):
    m3u_content = "#EXTM3U\n"
    for event in data.get("matches", []):
        name = event.get("name", "Unknown Event")
        url = event.get("url", "")
        # Aap apne mutabik extra tags (logo, group) insert kar sakte hain
        m3u_content += f'#EXTINF:-1, {name}\n{url}\n'
        
    with open("sonyliv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Successfully updated sonyliv.m3u!")

if __name__ == "__main__":
    fetch_and_update()
