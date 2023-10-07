import re

from youtube_transcript_api import YouTubeTranscriptApi

print(
    "Welcome to YouTube videos in a nutshell\nFor now, you can only get a .txt file with the transcript of the video you entered in its corresponding language\nLater on, you'll have features such as language selection, content summarizing and even a webpage for a more intuitive UI!"
)

video_code = input("Please enter your video code:\nEX: FuCEMRDWW7A\n")

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_code)
except Exception as e:
    print(
        f"It wasn't possible to get your video's transcript. Make sure your entering only the code of your desired video, not its URL. EX: FuCEMRDWW7A\n{e}"
    )

text_lines = []

for line in transcript:
    text_line = line["text"]
    if not re.search(r"\[.*\]", text_line):
        text_lines.append(text_line)

text = "\n".join(text_lines)

file_path = "transcript.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(text)

print("Your video transcript is now available at ./transcript.txt")
