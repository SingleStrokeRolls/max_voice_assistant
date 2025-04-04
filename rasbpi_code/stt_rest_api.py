from aip import AipSpeech
'''
APP_ID = "116055145"
API_KEY = "U5A8Q2peYEsvkQjjrh1zG0CF"
SECRET_KEY = "kronV08kWvGwNpAZLVwcfhLQEUhHJkc5"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
'''
#Read File
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def single_query_audio(client):
    response = client.asr(get_file_content('test.wav'), 'wav', 16000, {
        'dev_pid': 1737,
    })
    return response['result'][0]
