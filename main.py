import os
from download import download_videos
from extract_audio import extract_audio
from transcribe import transcribe_audio
from write_transcripts import write_transcripts

# Path to the cookies.txt file
cookies_path = r"C:\Users\mohan\OneDrive\Desktop\Tools\cookies.txt"

# List of video URLs to download
video_links = [
    "https://nyu.zoom.us/rec/play/4CP7hk6rPqudQ_ktNhHRKCy_1swT-7BwTE9gof9s_CexRQfGddIuBxkZ5efRU2wDrU7vGXO5GsGy9gyl.zVGGcpP7ctYnTOSt",
]

# List of downloaded MP4 files (replace these with actual file paths after downloading)
downloaded_videos = [
    "pc1.mp4",  # Replace with the actual path to your MP4 file
    "pc2.mp4",  # Add as many MP4 files as you need
    "pc3.mp4",
    "pc4.mp4"
]

# Uncomment the steps you want to execute

# Step 1: Download videos (Uncomment if you want to download videos)
# download_videos(video_links, cookies_path)

# Step 2: Extract audio from each video and transcribe
for video in downloaded_videos:
    # Generate corresponding WAV file name for each MP4
    audio_file = video.replace(".mp4", ".wav")
    
    # Extract audio
    print(f"Extracting audio for {video} to {audio_file}")
    extract_audio(video, audio_file)  # Ensure it passes the correct video and audio file

    # Step 3: Transcribe the audio
    print(f"Transcribing {audio_file}")
    transcript = transcribe_audio(audio_file, model_size="base")  # Ensure it passes the correct audio file

    # Step 4: Write the transcripts to files
    srt_filename = video.replace(".mp4", ".srt")
    combined_filename = video.replace(".mp4", "_c_transcript.txt")
    
    print(f"Saving transcripts: SRT -> {srt_filename}, Combined Text -> {combined_filename}")
    write_transcripts(transcript, srt_filename=srt_filename, combined_filename=combined_filename)
