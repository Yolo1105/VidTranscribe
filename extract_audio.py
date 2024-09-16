# extract_audio.py

import subprocess

def extract_audio(video_path, audio_output):
    try:
        print(f"Extracting audio from {video_path}...")
        subprocess.run(
            [
                "ffmpeg", 
                "-i", video_path, 
                "-q:a", "0", 
                "-map", "a", 
                audio_output
            ], 
            check=True
        )
        print(f"Audio extracted successfully and saved as {audio_output}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")
        return False
    return True
