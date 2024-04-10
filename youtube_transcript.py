import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(video_url):
    match = re.search(r"(?<=v=)[\w-]+", video_url)
    if match:
        return match.group(0)
    else:
        match = re.search(r"(?<=be/)[\w-]+", video_url)
        if match:
            return match.group(0)
        else:
            return None

def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    if video_id:
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript = ''
            for segment in transcript_list:
                transcript += segment['text'] + ' '
            return transcript.strip()
        except Exception as e:
            print("Error:", e)
            return None
    else:
        print("Invalid YouTube URL.")
        return None

youtube_url = params['text']
transcript = get_transcript(youtube_url)
if transcript:
    print(transcript)
else:
    print("Transcript not available.")
    
return transcript
    

