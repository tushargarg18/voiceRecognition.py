import numpy as np
import matplotlib.pyplot as plt

hex_data_str = input('Enter Data : \n')

hex_data_char_lst = hex_data_str.split(" ")
hex_data_lst = []
for i in range(0, len(hex_data_char_lst)):
    temp = int(hex_data_char_lst[i], 16)
    hex_data_lst.append(temp)

raw_voice_data = []
max = 0
for i in range(0, len(hex_data_lst), 2):
    temp = (hex_data_lst[i+1]<<8) | hex_data_lst[i]
    if(max < temp):
        max = temp
    raw_voice_data.append(temp)
print(max)
print(raw_voice_data)

raw_voice_data_np = np.array(raw_voice_data)
time_value_np = np.linspace(0, 1, len(raw_voice_data_np))

plt.plot(time_value_np, raw_voice_data_np)
plt.show()