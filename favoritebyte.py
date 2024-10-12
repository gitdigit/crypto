message = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte_msg = bytes.fromhex(message)
print(byte_msg)

for secret in range(256):
    decoding = bytes([secret^o for o in byte_msg])
    print(decoding)
