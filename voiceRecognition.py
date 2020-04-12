import speech_recognition as sr
import base64
import wave
import struct

r = sr.Recognizer()

myframerate = 32000
mychannel = 1
mysampleWidth = 2
duration = 12                   #edit duration of sound here
myframes = duration * myframerate

if __name__ == '__main__':
    encoded = input('Enter Base64 data!\n')
    decoded = base64.standard_b64decode(encoded)
    i = 0
    obj = wave.open('sound.wav', 'wb')
    obj.setnchannels(mychannel)
    obj.setsampwidth(mysampleWidth)
    obj.setframerate(myframerate)
    obj.setnframes(int(myframes))
    for i in range(0, len(decoded), 2):
        temp1 = ((decoded[i+1] << 8) | decoded[i])
        data = struct.pack('<i', temp1)
        obj.writeframesraw(data)
    print(i)
    obj.close()
    harvard = sr.AudioFile('sound.wav')
    with harvard as source:
        audio = r.record(source)
    print(r.recognize_google(audio))
