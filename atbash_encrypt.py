def atbash_encrypt(plaintext_file, ciphertext_file):
    """
    Encrypts the given plaintext_file using the Atbash method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :return: the encrypted *.txt file
    """
    atbash_alpha = 'zyxwvutsrqponmlkjihgfedcba'
    return substitution_encrypt(plaintext_file, ciphertext_file, atbash_alpha)