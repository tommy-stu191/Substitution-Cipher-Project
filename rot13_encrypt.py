def rot13_encrypt(plaintext_file, ciphertext_file):
    """
    Encrypts the given plaintext_file using the ROT-13 method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :return: the encrypted *.txt file
    """
    return caesar_encrypt(plaintext_file, ciphertext_file, 13)
