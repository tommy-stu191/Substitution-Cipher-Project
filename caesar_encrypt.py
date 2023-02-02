def caesar_encrypt(plaintext_file, ciphertext_file, shift: int):
    """
    Encrypts plaintext_file using Caesar Cipher, based on shift arg
    :param plaintext_file: Original .txt file to encrypt
    :param ciphertext_file: Final encryption of plaintext_file
    :param shift: Num of shifts to perform for caesar cipher
    :return:
    """
    cipher_list = shift_cipher(shift)
    cipher_alphabet = ''.join(cipher_list)
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
    return cipher
