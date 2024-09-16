# transcribe.py

from faster_whisper import WhisperModel

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
