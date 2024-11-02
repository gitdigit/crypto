def atbash_cipher(plain):
    cipher_text = ""
    for letter in plain:
        if letter.isalpha():
            # Determine if the letter is uppercase or lowercase
            if letter.islower():
                # 'a' maps to 'z', 'b' to 'y', ..., 'z' to 'a'
                new_letter = chr(ord('z') - (ord(letter) - ord('a')))
            else:
                # 'A' maps to 'Z', 'B' to 'Y', ..., 'Z' to 'A'
                new_letter = chr(ord('Z') - (ord(letter) - ord('A')))
            cipher_text += new_letter
        else:
            # Non-alphabet characters are added directly
            cipher_text += letter
    return cipher_text

def caesar_cipher_atbash(text):
    atbash_text = atbash_cipher(text)
    print(f"The Atbash cipher text is: {atbash_text}")

end_game = False
while not end_game:
    text = input("Say what you want (will be processed with Atbash cipher):\n")
    caesar_cipher_atbash(text)
    if input("Do you want to quit? (y/n) ").lower() == "y":
        end_game = True
