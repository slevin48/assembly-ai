import os
import requests
from dotenv import load_dotenv

load_dotenv()

transcription_id = input("Transcription id: ")

endpoint = f"https://api.assemblyai.com/v2/transcript/{transcription_id}"
headers = {
    "authorization": os.environ["API_KEY"],
}
response = requests.get(
    endpoint,
    headers=headers,
)
t = response.json()['text']
print(t)