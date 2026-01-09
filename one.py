import requests
import os

image_url = "https://krconnect.mkce.ac.in/images/sphoto/20251029_101033_B156.JPG"
save_dir = r"E:/B1"
file_name = "20251029_101033_B156.JPG"

# Ensure directory exists (old-school discipline meets modern ops)
os.makedirs(save_dir, exist_ok=True)

file_path = os.path.join(save_dir, file_name)

try:
    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    with open(file_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    print(f"✅ File successfully stored at: {file_path}")

except requests.exceptions.RequestException as e:
    print(f"❌ Download failed: {e}")
