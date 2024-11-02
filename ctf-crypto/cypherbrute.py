logo = """
  _____                             _____ _       _             
 / ____|                           / ____(_)     | |            
| |     __ _  ___  ___  __ _ _ __ | |     _ _ __ | |_ ___  _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|| |    | | '_ \| __/ _ \| '__|
| |___| (_| |  __/\__ \ (_| | |   | |____| | | | | || (_) | |   
 \_____\__,_|\___||___/\__,_|_|    \_____|_|_| |_|\__\___/|_|   

"""
print(logo)

def encryptage(plain, shiftnb):
    cipher_text = ""
    for letter in plain:
        if letter.isalpha():
            start = ord('a') if letter.islower() else ord('A')
            new_letter = chr((ord(letter) - start + shiftnb) % 26 + start)
            cipher_text += new_letter
        else:
            cipher_text += letter
    return cipher_text

def decryptage(the_text, the_shift):
    return encryptage(the_text, -the_shift)

def try_all_shifts(cipher_text):
    print("\nAttempting all possible shifts:")
    for shift in range(1, 26):
        decoded_text = decryptage(cipher_text, shift)
        print(f"Shift {shift}: {decoded_text}")

def caesar_cipher(shift_amount, cipher_direction):
    if cipher_direction == "encode":
        new_text = encryptage(text, shift_amount)
        print(f"The encoded text is: {new_text}")
    elif cipher_direction == "decode":
        new_text = decryptage(text, shift_amount)
        print(f"The decoded text is: {new_text}")
    elif cipher_direction == "brute":
        try_all_shifts(text)

end_game = False
while not end_game:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'brute' to try all shifts:\n").lower()
    text = input("Say what you want: \n")
    if direction in ["encode", "decode"]:
        shift = int(input("Type the shift number:\n"))
        caesar_cipher(shift, direction)
    elif direction == "brute":
        caesar_cipher(0, direction)
    if input("Do you want to quit? (y/n) ").lower() == "y":
        end_game = True
