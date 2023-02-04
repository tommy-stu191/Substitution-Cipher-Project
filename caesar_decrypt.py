def caesar_decrypt(ciphertext_file, plaintext_file, shift: int):
    """
    Decrypts the given ciphertext_file using the caesar method with the given shift.
    :param ciphertext_file: the pre-defined encoded *.txt file
    :param plaintext_file: the decoded file to be returned
    :param shift: an integer, the amount of places to shift to the right
    :return: a decoded *.txt file
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, -shift)
