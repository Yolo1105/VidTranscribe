# download.py

import subprocess

def download_videos(links, cookies):
    for link in links:
        print(f"Downloading video: {link}")
        try:
            subprocess.run(
                [
                    "yt-dlp", 
                    "--cookies", cookies, 
                    link
                ], 
                check=True
            )
            print(f"Downloaded successfully: {link}")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {link}: {e}")
