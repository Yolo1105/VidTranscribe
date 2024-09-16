import os
import subprocess
from faster_whisper import WhisperModel

# Path to the cookies.txt file
cookies_path = r"C:\Users\mohan\OneDrive\Desktop\Tools\cookies.txt"

# List of video URLs to download
video_links = [
    "https://nyu.zoom.us/rec/play/4CP7hk6rPqudQ_ktNhHRKCy_1swT-7BwTE9gof9s_CexRQfGddIuBxkZ5efRU2wDrU7vGXO5GsGy9gyl.zVGGcpP7ctYnTOSt",
]

# Step 1: Download the video
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

# Step 2: Extract audio from the downloaded video using ffmpeg
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

# Step 3: Transcribe the audio file using faster-whisper
def transcribe_audio(audio_path, model_size="base"):
    print(f"Loading Whisper model ({model_size})...")
    model = WhisperModel(model_size)
    
    print(f"Transcribing audio file {audio_path}...")
    segments, info = model.transcribe(audio_path)

    print(f"Transcription info: {info}")
    transcript = []
    for i, segment in enumerate(segments, start=1):
        start = format_time(segment.start)
        end = format_time(segment.end)
        transcript.append(f"{i}\n{start} --> {end}\n{segment.text.strip()}\n")
    
    return transcript

# Helper function to format time into the SRT time format
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

# Step 4: Write the SRT transcript and combine into a complete transcript
def write_transcripts(transcript, srt_filename="transcript.txt", combined_filename="c_transcript.txt"):
    with open(srt_filename, "w") as srt_file:
        srt_file.write("\n".join(transcript))
    print(f"SRT transcript saved as '{srt_filename}'")
    
    # Combine all segments into a single text
    combined_transcript = " ".join([segment.split("\n")[2] for segment in transcript])
    with open(combined_filename, "w") as combined_file:
        combined_file.write(combined_transcript)
    print(f"Combined transcript saved as '{combined_filename}'")

if __name__ == "__main__":
    # Step 1: Download videos
    download_videos(video_links, cookies_path)
    
    # Assuming the video is downloaded and you know the video file name.
    # Replace 'downloaded_video.mp4' with the actual name of the downloaded video.
    downloaded_video = "downloaded_video.mp4"  # This should be the actual downloaded file name
    audio_file = "extracted_audio.wav"
    
    # Step 2: Extract audio from the video
    if extract_audio(downloaded_video, audio_file):
        # Step 3: Transcribe the audio
        transcript = transcribe_audio(audio_file, model_size="base")
        
        # Step 4: Write the transcripts to files
        write_transcripts(transcript, srt_filename="transcript.txt", combined_filename="c_transcript.txt")
