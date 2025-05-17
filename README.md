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
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure `ffmpeg` is installed and accessible:

- On macOS: `brew install ffmpeg`
- On Ubuntu: `sudo apt install ffmpeg`
- On Windows: Download from [ffmpeg.org](https://ffmpeg.org/)

4. Set your Gemini API key:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

(Windows PowerShell)

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

---

## Usage

```bash
python script.py <youtube_url>
```

Example:

```bash
python script.py https://youtu.be/KOgsOiweR4Q
```

The script will:

- Download the video and audio
- Convert to MP3
- Upload to Gemini for transcription
- Output the SRT subtitles to the console
- Copy the SRT subtitles to your clipboard automatically

---

## Notes

- Temporary files are saved in your system temp folder.
- Only videos with 1080p or higher resolution are downloaded.
- The transcription prompt asks Gemini to produce clean SRT subtitle files without extra text.
- Make sure your API key has access to the Gemini API.

---

## License

MIT License — feel free to use and modify!

---

If you have questions or want features, open an issue or pull request!

