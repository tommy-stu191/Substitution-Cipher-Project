def substitution_decrypt(ciphertext_file, plaintext_file, cipher_alphabet):
    """
    Decrypts the given ciphertext_file using the substitution method.
    :param ciphertext_file: The *.txt file being decrypted
    :param plaintext_file: The name of the *.txt file returned
    :param cipher_alphabet: A string "key" for the encryption
    :return: A *.txt plaintext file
    """
    return substitution_encrypt(ciphertext_file, plaintext_file, cipher_alphabet)




