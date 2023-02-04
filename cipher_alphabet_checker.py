def cipher_alphabet_checker(cipher_alphabet):
    """
    Checks validity of the cipher_alphabet string.
    :param cipher_alphabet: a string of letters
    :return: a T/F boolean value
    """
    # Converting the string into a list and set for comparison
    cipher_list = cipher_alphabet_to_list(cipher_alphabet)
    cipher_set = set(cipher_list)
    # Using conditionals to test the validity of cipher_alphabet
    if (len(cipher_list) == 26) and\
            (len(cipher_list) == len(cipher_set)) and\
            (cipher_alphabet.isalpha() and
             (cipher_alphabet.islower())):
        return True
    return False

