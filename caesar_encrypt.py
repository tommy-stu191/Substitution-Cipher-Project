def caesar_encrypt(plaintext_file, ciphertext_file, shift: int):
    cipher_list = shift_cipher(shift)
    cipher_alphabet = ''.join(cipher_list)
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
    return cipher
