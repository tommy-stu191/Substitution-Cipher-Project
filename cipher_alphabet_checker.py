def cipher_alphabet_checker(cipher_alphabet):
    """
    Checks that cipher alphabet given, meet specifications:
    1. 26 Chars
    2. No duplicates
    3. ...
    :param cipher_alphabet: a string of letters
    :return: a T/F boolean value
    """

    cipher_list = cipher_alphabet_to_list(cipher_alphabet)
    cipher_set = set(cipher_list)

    if (len(cipher_list) == 26) and\
            (len(cipher_list) == len(cipher_set)) and\
            (cipher_alphabet.isalpha() and
             (cipher_alphabet.islower())):
        return True
    return False
