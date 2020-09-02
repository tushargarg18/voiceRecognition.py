import  base64
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
encoded_input = input('Enter base64 String')
#decoded = base64.standard_b64decode(encoded_input)
#print(decoded)
added_48bits = []
decoded_output = []
for i in range(0, len(encoded_input)-7, 8):
    temp = 0
    for j in range(0, 8):
        #print(base64_chars.find(encoded_input[i+j]))
        temp = temp + base64_chars.find(encoded_input[i+j])
        temp = temp * 64
    added_48bits.append(temp)
for i in range(0, len(added_48bits)):
    for j in range(0, 3):
        #temp = (int((added_48bits[i] / (2 ^ (32 - (j*16))))) & 0xffff)
        temp = ((added_48bits[i] >> (48-16*(j+1))) & 0xFFFF)
        decoded_output.append(int(temp))
print(decoded_output)
#print(added_48bits)
print(len(encoded_input))
