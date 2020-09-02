import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

r = sr.Recognizer()

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encoded_data = input('Enter the data : \n')

myframerate = 32000
mychannel = 1
mysampleWidth = 2
duration = 9  # edit duration of sound here
myframes = duration * myframerate

if __name__ == '__main__':
    obj = wave.open('sound_new_encoding.wav', 'wb')
    obj.setnchannels(mychannel)
    obj.setsampwidth(mysampleWidth)
    obj.setframerate(myframerate)
    obj.setnframes(int(myframes))
    count = 0
    useful_data = ''
    Useless_data = ''
    i = 0
    voice_data = []
    while(i < len(encoded_data)):
    #for i in range(0, len(encoded_data), 2):
        if((base64_chars.find(encoded_data[i+1]) != -1) & (base64_chars.find(encoded_data[i]) != -1)):
            temp = (base64_chars.find(encoded_data[i+1]) << 6) | base64_chars.find((encoded_data[i]))
            #if(temp >= 1000):
            voice_data.append(temp)
            useful_data += encoded_data[i]
            useful_data += encoded_data[i+1]
            count = count + 1
            data = struct.pack('<i', temp)
            obj.writeframesraw(data)
        else:
            Useless_data += encoded_data[i]
            Useless_data += encoded_data[i+1]
        i += 2
    obj.close()
    voice_data_np = np.array(voice_data)
    time = np.linspace(0, 18, len(voice_data))
    plt.plot(time, voice_data_np)
    plt.show()

    harvard = sr.AudioFile('sound_new_encoding.wav')
    with harvard as source:
        audio = r.record(source)
    print(r.recognize_google(audio))
    count *= 2
    print(count)
    print(len(useful_data))
    print(len(encoded_data))
    print(len(Useless_data))
    print(Useless_data)

