def rot13_encrypt(plaintext_file, ciphertext_file):
    """
    Encrypts .txt files based on rot-13 cipher
    :param plaintext_file: Original file to encrypt
    :param ciphertext_file: Encrypted file
    :return:
    """
    return caesar_encrypt(plaintext_file, ciphertext_file, 13)
