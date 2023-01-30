def substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet):
    """

    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param cipher_alphabet: a string, the encryption pattern
    :return: a *.txt file containing the encrypted message
    """

    # Testing validity of cipher_alphabet
    if not cipher_alphabet_checker(cipher_alphabet):
        print("Invalid cipher_alphabet")
        exit()

    # Converting the file & string to lists
    plaintext_list = textfile_to_list(plaintext_file)
    cipher_list = cipher_alphabet_to_list(cipher_alphabet)

    ciphertext_list = _crypter(plaintext_list, cipher_list)

    ciphertext_file = list_to_textfile(ciphertext_list, ciphertext_file)

    return ciphertext_file
