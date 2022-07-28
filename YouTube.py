"""
To download YouTube videos by providing a link to your code in Python
"""

# Install the  package :  pip install youtube_dl
# install the package emoji for ..............


# The following code to download the video to our environment
import youtube_dl
import emoji

ydl_opt = {}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    # The Download will start and the video in mp4 format would be available!
    ydl.download(["https://www.youtube.com/watch?v=NLrfVMWT4AI"])
print(
    emoji.emojize("Download from YouTube via Python is cool :thumbs_up")
)  # with the package , we can have the emoji output in terminal


# Terminal:
# [youtube] NLrfVMWT4AI: Downloading webpage
# [download] Destination: the BEST way to get Kali Linux!!-NLrfVMWT4AI.mp4
# [download]   3.9% of 21.99MiB at 74.27KiB/s ETA 04:51
