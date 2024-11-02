def rot47(char, shift):
    if 33 <= ord(char) <= 126:
        return chr(33 + ((ord(char) - 33 + shift) % 94))
    return char

def decode_rot47(encoded_str, shift):
    decoded_str = ''.join(rot47(char, shift) for char in encoded_str)
    return decoded_str

encoded_string = "$E2Cw24<LrbDcccC0cF0|JDEbCb05b0=c0$c=c5bN"

for shift in range(1, 63):
    decoded_string = decode_rot47(encoded_string, shift)
    print(f"Shift {shift}: {decoded_string.replace(' ', '')}")