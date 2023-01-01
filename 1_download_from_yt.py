import os, pytube

d = "https://www.youtube.com/watch?v=TUVcZfQe-Kw"
url = (input("URL of the Youtube video to download (leave blank for default):\nhttps://www.youtube.com/watch?v=TUVcZfQe-Kw\n") or d)

# Dowload Youtube Video (audio only)
yt = pytube.YouTube(url)
video = yt.streams.filter(only_audio=True).first()   
title = video.title
print(f'Getting {title}')

out_file = video.download('downloads')
print(f'Downloaded in {out_file}')

# Video to Audio
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
if not os.path.exists(new_file):
    os.rename(out_file, new_file)

print((f'Downloaded in {new_file}'))
