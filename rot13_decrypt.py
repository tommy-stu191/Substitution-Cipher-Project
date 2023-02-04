def rot13_decrypt(ciphertext_file, plaintext_file):
    """
    Decrypts the given ciphertext_file using the ROT-13 method.
    :param ciphertext_file: the pre-defined encoded *.txt file
    :param plaintext_file: the decoded file to be returned
    :return: a decoded *.txt file
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, -13)
