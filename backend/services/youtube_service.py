from youtube_transcript_api import YouTubeTranscriptApi

import re


def extract_video_id(url):

    match = re.search(r"v=([^&]+)", url)

    if match:
        return match.group(1)

    return None


def fetch_youtube_transcript(url):

    try:

        video_id = extract_video_id(url)

        if not video_id:
            return "Invalid YouTube URL"

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        text = " ".join([
            snippet.text
            for snippet in transcript
        ])

        return text

    except Exception as e:

        return f"Transcript fetch failed: {str(e)}"