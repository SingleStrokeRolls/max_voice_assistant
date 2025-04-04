from volcenginesdkarkruntime import Ark
from aip import AipSpeech
from volc import single_query_text
from tts_rest_api import single_query_speech
from stt_rest_api import single_query_audio
import sender_client, receiver_client
import os

#Keys
APP_ID = "116055145"
API_KEY = "U5A8Q2peYEsvkQjjrh1zG0CF"
SECRET_KEY = "kronV08kWvGwNpAZLVwcfhLQEUhHJkc5"

#clients
text_client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)
speech_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#print("Hey man this is max. How can I help you today?")
receiver_client.do_receive()

question = single_query_audio(speech_client)

answer = single_query_text(text_client, question)

success = single_query_speech(speech_client, answer)

if success:
    os.system(f'ffmpeg -y -i audio.mp3 output.wav')

sender_client.do_send()
