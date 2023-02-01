import helper_functions
import substitution_encrypt


def caesar_cipher(shift: int, plain_textfile, cipher_textfile, cipher_alphabet):
    cipher_alphabet = helper_functions.shift_cipher(shift, cipher_alphabet)
    cipher = substitution_encrypt.substitution_encrypt(plain_textfile, cipher_textfile, cipher_alphabet)
    return cipher
