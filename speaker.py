from machine import I2S
from machine import Pin

def do_speak():

    # 定义I2S引脚
    sck_pin = Pin(12)
    ws_pin = Pin(14)
    sd_pin = Pin(13)

    # 初始化I2S
    audio_out = I2S(1, sck=sck_pin, ws=ws_pin, sd=sd_pin, mode=I2S.TX, bits=16, format=I2S.MONO, rate=16000, ibuf=20000)
    # 打开WAV文件并播放
    wav_file = "output.wav"
    with open(wav_file, 'rb') as f:
        f.seek(44)  # 跳过WAV文件头
        wav_samples = bytearray(1024)
        wav_samples_mv = memoryview(wav_samples)
        print("Speaking...")
        while True:
            num_read = f.readinto(wav_samples_mv)
            if num_read == 0:
                break
            num_written = 0
            while num_written < num_read:
                num_written += audio_out.write(wav_samples_mv[num_written:num_read])
