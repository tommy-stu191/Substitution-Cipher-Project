def keyword_encrypt(plaintext_file, ciphertext_file, keyword, is_keyword_decrypt=None):
    """
    Encrypts the given plaintext_file using the given keyword and the Keyword method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :param keyword: string that defines the cipher
    :param is_keyword_decrypt: optional parameter, takes a boolean value
    :return: the encrypted *.txt file
    """
    # Checking the validity of keyword
    if not keyword_check(keyword):
        print("Invalid keyword")
        exit()

    # Creating the cipher alphabet
    cipher_list = keyword_to_cipherlist(keyword)
    cipher_alphabet = ''.join(cipher_list)

    if is_keyword_decrypt:
        return substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet, is_keyword_decrypt=True)
    else:
        return substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
