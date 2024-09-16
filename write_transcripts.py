# write_transcripts.py

def write_transcripts(transcript, srt_filename="transcript.srt", combined_filename="c_transcript.txt"):
    # Write the SRT file
    with open(srt_filename, "w") as srt_file:
        srt_file.write("\n".join(transcript))
    print(f"SRT transcript saved as '{srt_filename}'")
    
    # Write the combined transcript (comma-separated)
    combined_transcript = ", ".join([segment.split("\n")[2] for segment in transcript])
    with open(combined_filename, "w") as combined_file:
        combined_file.write(combined_transcript)
    print(f"Combined transcript saved as '{combined_filename}'")
