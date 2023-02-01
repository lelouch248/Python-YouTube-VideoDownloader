from pytube import YouTube
from sys import argv


link = "https://youtu.be/vEQ8CXFWLZU"
yt = YouTube(link)

print("title: ",yt.title)
print("view: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('downloaded-video')

