# from wlan import do_connect
# from sender_client import do_send
# from receiver_client import do_receive
import sender_client, Recorder_mod, receiver_client, speaker, wlan

wlan.do_connect()

Recorder_mod.do_record()

sender_client.do_send()

receiver_client.do_receive()

speaker.do_speak()

