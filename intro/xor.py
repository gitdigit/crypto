word = "label"
word_list = []
unicode_word = [ord(char) for char in word]
xor_operation = [13^o for o in unicode_word]
xor_word = ["".join(chr(o) for o in xor_operation)]
print(xor_word)

