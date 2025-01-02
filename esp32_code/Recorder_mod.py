from machine import I2S,SPI
from machine import Pin
#from WAVESaveUitl import *
import utime

def do_record():

    sampleRate = 8000
    bitsPerSample = 16
    bufSize = 32768
    datasize = bufSize * 4

    sck_pin = Pin(23)
    ws_pin = Pin(22)
    sd_pin = Pin(21)

    audioInI2S = I2S(0,
        sck=sck_pin, ws=ws_pin,sd=sd_pin,
        mode=I2S.RX,
        bits=bitsPerSample,
        format=I2S.STEREO,
        rate=sampleRate,
        ibuf=bufSize)
    readBuf = bytearray(bufSize)

    def createWavHeader(sampleRate, bitsPerSample, num_channels, datasize):    
        o = bytes("RIFF",'ascii')                                                   # (4byte) Marks file as RIFF
        o += (datasize + 36).to_bytes(4,'little')                                   # (4byte) File size in bytes excluding this and RIFF marker
        o += bytes("WAVE",'ascii')                                                  # (4byte) File type
        o += bytes("fmt ",'ascii')                                                  # (4byte) Format Chunk Marker
        o += (16).to_bytes(4,'little')                                              # (4byte) Length of above format data
        o += (1).to_bytes(2,'little')                                               # (2byte) Format type (1 - PCM)
        o += (num_channels).to_bytes(2,'little')                                    # (2byte)
        o += (sampleRate).to_bytes(4,'little')                                      # (4byte)
        o += (sampleRate * num_channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
        o += (num_channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
        o += (bitsPerSample).to_bytes(2,'little')                                   # (2byte)
        o += bytes("data",'ascii')                                                  # (4byte) Data Chunk Marker
        o += (datasize).to_bytes(4,'little')                                        # (4byte) Data size in bytes
        return o
    headData = createWavHeader(sampleRate,bitsPerSample,2,datasize)
    fOut = open("test.wav","wb")
    fOut.write(headData)
    print("ready...")
    utime.sleep(1.0)
    byteCount=0
    while True:
        currByteCount = audioInI2S.readinto(readBuf)
        fOut.write(readBuf)
        byteCount = byteCount + currByteCount
        if byteCount >= datasize:
            break
    fOut.close()
    audioInI2S.deinit()
    print("finish.")
