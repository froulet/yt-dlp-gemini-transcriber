# yt-dlp-gemini-subtitle

A Python script that downloads a YouTube video (1080p+), extracts audio, and uses Google Gemini to transcribe it into SRT subtitle format.

The SRT transcript is copied to your clipboard for easy pasting!

---

## Features

- Downloads YouTube video with best quality (video + audio)
- Converts video to MP3 audio using ffmpeg
- Sends audio to Google Gemini for transcription with timestamps
- Outputs SRT subtitle format (no extra commentary)
- Copies SRT text automatically to clipboard

---

## Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- ffmpeg installed and available in your system PATH
- Google Gemini API access and API key set as environment variable `GEMINI_API_KEY`
- Python packages listed in `requirements.txt` (see below)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/yt-dlp-gemini-subtitle.git
cd yt-dlp-gemini-subtitle
