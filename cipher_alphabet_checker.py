def cipher_alphabet_checker(cipher_alphabet, cipher_alphabet_list):
    """

    :param cipher_alphabet: a string of letters
    :param cipher_alphabet_list: a list of cipher_alphabet
    :return: a boolean value
    """

    cipher_alphabet_set = set(cipher_alphabet_list)

    if (len(cipher_alphabet_list) == 26) \
            and (len(cipher_alphabet_list) == len(cipher_alphabet_set)) \
            and (cipher_alphabet.isalpha()):
        return True
    return False
