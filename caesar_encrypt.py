def caesar_encrypt(plaintext_file, ciphertext_file, shift: int):
    """
    Encrypts the given plaintext_file using the caesar method with the given shift.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :param shift: an integer, the amount of places to shift
    :return: the encrypted *.txt file
    """
    cipher_list = shift_cipher(shift)
    cipher_alphabet = ''.join(cipher_list)
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
    return cipher
