from Crypto.Util.number import *

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key3_key2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
f_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

byte_key1 = bytes.fromhex(key1)
byte_key2_key1 = bytes.fromhex(key2_key1)
byte_key3_key2 = bytes.fromhex(key3_key2)
byte_f = bytes.fromhex(f_hex)

print("Transformation du hex1 en byte", byte_key1)
print("Transformation du hex2^hex1 en byte", byte_key2_key1)
print("Transformation du hex3^hex2 en byte", byte_key3_key2)
print("Transformation du FLAG ^ KEY1 ^ KEY3 ^ KEY2  en byte", byte_f)

print(len(byte_key1))
print(len(byte_key2_key1))
print(len(byte_key3_key2))
print(len(byte_f))

byte_key2 = bytes([k1^k2 for k1, k2 in zip(byte_key1, byte_key2_key1)])
print("C'est key2 mais en bytes",byte_key2)

key2_hex = byte_key2.hex()
print("C'est key2 mais en hex", key2_hex)

byte_key3 = bytes([k3_k2^k2 for k3_k2, k2 in zip (byte_key3_key2, byte_key2)])
print("C'est key3 mais en bytes", byte_key3)

key3_hex = byte_key3.hex()
print("C'est key3 mais en hex", key3_hex)

flag = bytes([f^(k1^(k3^k2)) for f, k1, k3, k2 in zip(byte_f, byte_key1, byte_key3, byte_key2)])
print(flag)

