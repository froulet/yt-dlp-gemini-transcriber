import os
import sys
import subprocess
import tempfile
from pathlib import Path

import yt_dlp
import pyperclip
from google import genai
from google.genai import types

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]

    # Use system temp directory and descriptive base filename
    temp_dir = Path(tempfile.gettempdir())
    file_stem = temp_dir / "yt_gemini_subtitle"
    video_path = file_stem.with_suffix(".mp4")
    mp3_path = file_stem.with_suffix(".mp3")

    ydl_opts = {
        "outtmpl": str(file_stem) + ".%(ext)s",
        "restrictfilenames": True,
        "format": "bestvideo[height>=1080]+bestaudio/best",
        "merge_output_format": "mp4",
    }

    # Download YouTube video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("🎥 YouTube video downloaded!")

    # Convert MP4 to MP3
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", "-acodec", "libmp3lame", "-q:a", "6", str(mp3_path)
    ], check=True)

    PROMPT = """
    Please transcribe the audio file I’m providing, including timestamps for each line, and format it as an SRT file. Only output the SRT content, without any additional text or commentary.

    Example output:
    1
    00:00:00,000 --> 00:00:02,500
    Welcome to the Example Subtitle File!

    2
    00:00:03,000 --> 00:00:06,000
    This is a demonstration of SRT subtitles.

    3
    00:00:07,000 --> 00:00:10,500
    You can use SRT files to add subtitles to your videos.
    """

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    uploaded_file = client.files.upload(file=str(mp3_path))

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        contents=[PROMPT, uploaded_file],
        config=types.GenerateContentConfig(
            safety_settings=[
                types.SafetySetting(category=cat, threshold="BLOCK_NONE")
                for cat in [
                    "HARM_CATEGORY_HARASSMENT",
                    "HARM_CATEGORY_HATE_SPEECH",
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "HARM_CATEGORY_CIVIC_INTEGRITY",
                ]
            ]
        ),
    )

    srt_text = response.text.replace("```srt", "").replace("```", "").strip()
    pyperclip.copy(srt_text)
    print(srt_text)


if __name__ == "__main__":
    main()
