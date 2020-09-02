import speech_recognition as sr
import struct
import base64
import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft

r = sr.Recognizer()

myframerate = 88000
mychannel = 1
mysampleWidth = 2
duration = 7  # edit duration of sound here
myframes = duration * myframerate

if __name__ == '__main__':
    encoded = input('Enter Base64 data!\n')
    decoded = base64.standard_b64decode(encoded)
    i = 0
    obj = wave.open('sound_44KHz.wav', 'wb')
    obj.setnchannels(mychannel)
    obj.setsampwidth(mysampleWidth)
    obj.setframerate(myframerate)
    obj.setnframes(int(myframes))
    voice_sample = []
    for i in range(0, (len(decoded)//7)*7, 2):
        temp1 = ((decoded[i + 1] << 8) | decoded[i])
        # if(temp1 >= 4096):
        #     temp1 = 0
        # else:
        #     temp1 = temp1 * 5
        voice_sample.append(temp1)
        data = struct.pack('<i', temp1)
        obj.writeframesraw(data)
    obj.close()
    harvard = sr.AudioFile('sound_new_encoding.wav')
    with harvard as source:
        audio = r.record(source)
    print(r.recognize_google(audio))
    voice_samples_np = np.array(voice_sample)
    frequencies = fft(voice_samples_np)
    time_values = np.linspace(0, 7, len(voice_sample))
    print(frequencies)
   # plt.plot(time_values, frequencies, 'ro')
   # plt.show()
