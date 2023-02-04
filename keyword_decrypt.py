def keyword_decrypt(ciphertext_file, plaintext_file, keyword):
    """
    Decrypts the given ciphertext_file using the given keyword and the Keyword method.
    :param plaintext_file: the new decrypted *.txt file
    :param ciphertext_file: the encrypted *.txt file
    :param keyword: string that defines the cipher
    :return: the decrypted *.txt file
    """
    return keyword_encrypt(ciphertext_file, plaintext_file, keyword, is_keyword_decrypt=True)
