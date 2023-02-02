def rot13_decrypt(ciphertext_file, plaintext_file):
    """
    Decrypts .txt file based on rot-13 cipher
    :param ciphertext_file: Encrypted file to decrypt
    :param plaintext_file: Final decryption of ciphertext_file
    :return: A *.txt plaintext file
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, -13)
