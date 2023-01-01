import os
import requests
from dotenv import load_dotenv

load_dotenv()

# file = input("Local file to upload:")

l = os.listdir('downloads')
for idx, item in enumerate(l):
    print(idx, item)
i = int(input("Location of the file to upload: "))
file = 'downloads/'+l[i]
print(file)

# Upload local file to AssemblyAI
headers = {"authorization": os.environ["API_KEY"]}
res = requests.post(
    "https://api.assemblyai.com/v2/upload",
    headers=headers,
    data=open(file,'rb'),
)
upload_url = res.json()['upload_url']
print(upload_url)

# Transcript audio file
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {"audio_url": upload_url}
headers = {
    "authorization": os.environ["API_KEY"],
    "content-type": "application/json",
}
res = requests.post(
    endpoint,
    json=json,
    headers=headers,
)
transcription_id = res.json()['id']
print(transcription_id)