import string


def caesar_cipher(plaintext, shift):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def break_caesar_cipher(ciphertext, known_word):
    for shift in range(len(string.ascii_uppercase)):
        if known_word in caesar_cipher(ciphertext, shift).split():
            decrypted_message = caesar_cipher(ciphertext, shift)
            return decrypted_message
