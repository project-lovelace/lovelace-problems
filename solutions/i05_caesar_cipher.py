import string

def caesar_cipher(plaintext, shift):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

ciphertext = input()
known_word = input()

for shift in range(len(string.ascii_uppercase)):
    if known_word in caesar_cipher(ciphertext, shift).split():
        decrypted_message = caesar_cipher(ciphertext, shift)
        break

print(decrypted_message)
