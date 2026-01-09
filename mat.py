import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

BASE = "https://krconnect.mkce.ac.in/images/sphoto/"
SAVE_DIR = r"E:/photos_2025"   # Windows drive path

# Create target directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Option 1: If you have a list of known filenames, add them here
KNOWN_FILES = [
    # "20251029_101033_B156.JPG",
    # Add more filenames here if you know them
]

print("🔍 Attempting to access directory listing...")
resp = requests.get(BASE)

if resp.status_code == 403:
    print("⚠️  403 Forbidden: Directory listing is not accessible.")
    
    if KNOWN_FILES:
        print(f"📥 Downloading {len(KNOWN_FILES)} known files...")
        downloaded = 0
        for filename in KNOWN_FILES:
            file_url = BASE + filename
            try:
                r = requests.get(file_url, timeout=10)
                if r.status_code == 200:
                    file_path = os.path.join(SAVE_DIR, filename)
                    with open(file_path, "wb") as f:
                        f.write(r.content)
                    print(f"✅ Downloaded: {filename}")
                    downloaded += 1
                else:
                    print(f"❌ Not found: {filename}")
            except Exception as e:
                print(f"❌ Error downloading {filename}: {e}")
        
        print(f"\n✅ Downloaded {downloaded}/{len(KNOWN_FILES)} files")
    else:
        print("💡 Trying pattern-based download...")
        print("   Pattern: YYYYMMDD_HHMMSS_ID.JPG")
        print("   Date range: 20251020 to 20251110")
        print("   Sampling common times and IDs...\n")
        
        downloaded = 0
        
        # Generate dates from 20251020 to 20251110
        start_date = datetime(2025, 10, 29)
        end_date = datetime(2025, 11, 10)
        current_date = start_date
        
        while current_date <= end_date:
            date_str = current_date.strftime("%Y%m%d")
            print(f"📅 Checking date: {date_str}")
            
            day_downloads = 0
            # Sample times throughout the day (every 30 minutes)
            for h in range(0, 24):
                for m in [0, 30]:
                    for s in [0, 15, 30, 45]:
                        time_str = f"{h:02d}{m:02d}{s:02d}"
                        
                        # Try common ID patterns (B1-B200)
                        for id_num in range(1, 201):
                            filename = f"{date_str}_{time_str}_B{id_num}.JPG"
                            file_url = BASE + filename
                            
                            try:
                                r = requests.get(file_url, timeout=2, stream=True)
                                if r.status_code == 200:
                                    # Check if it's actually an image (not an error page)
                                    content_type = r.headers.get('Content-Type', '')
                                    if 'image' in content_type or len(r.content) > 10000:
                                        file_path = os.path.join(SAVE_DIR, filename)
                                        with open(file_path, "wb") as f:
                                            f.write(r.content)
                                        print(f"  ✅ {filename}")
                                        downloaded += 1
                                        day_downloads += 1
                            except:
                                pass
            
            print(f"  📊 Found {day_downloads} files for {date_str}")
            
            # Move to next day
            current_date += timedelta(days=1)
        
        if downloaded > 0:
            print(f"\n🎉 Total downloaded: {downloaded} files")
        else:
            print("\n❌ No files found. Consider adding known filenames to KNOWN_FILES list.")
            print("   Or the files may not be publicly accessible.")

elif resp.status_code == 200:
    print("✅ Directory accessible, parsing links...")
    soup = BeautifulSoup(resp.text, "html.parser")
    
    downloaded = 0
    for link in soup.find_all("a"):
        href = link.get("href", "")
        # Extract filename from href
        filename = href.split("/")[-1] if "/" in href else href
        
        if filename.startswith("2025") and filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # Use the full href if it's a complete URL, otherwise append to BASE
            if href.startswith("http"):
                file_url = href
            else:
                file_url = BASE + filename
            file_path = os.path.join(SAVE_DIR, filename)

            print(f"📥 Downloading: {filename}")
            
            try:
                r = requests.get(file_url, timeout=10)
                if r.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(r.content)
                    downloaded += 1
                else:
                    print(f"   ⚠️  Failed (Status: {r.status_code})")
            except Exception as e:
                print(f"   ❌ Error: {e}")
    
    if downloaded > 0:
        print(f"\n✅ Downloaded {downloaded} files successfully!")
    else:
        print("\n⚠️  No files starting with '2025' found in directory.")
else:
    print(f"❌ Failed to access URL (Status: {resp.status_code})")

print(f"\n📁 Files saved to: {SAVE_DIR}")
