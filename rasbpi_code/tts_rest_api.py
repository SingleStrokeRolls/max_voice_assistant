#from aip import AipSpeech

'''YOUR APP API SECRET'''

'''
APP_ID = "Your ID"
API_KEY = "Your Key"
SECRET_KEY = "Your key"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
'''

def single_query_speech(client,text_to_speech):
    result  = client.synthesis(text_to_speech,'en',1,{
        'vol':5,
        'per':3,
        'pit':7,
        'spd':8,
        })

    if not isinstance(result, dict):
        #print("here")
        with open('audio.mp3', 'wb') as f:
            f.write(result)
        return True
    else:
        print("error")
        return False
