def _crypter(plaintext_list, cipher_list):
    """

    :param plaintext_list: list of characters from plaintext_file
    :param cipher_list: a list of the cipher key
    :return: a(n) encrypted/decrypted list, ciphertext_list
    """
    ciphertext_list = []
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    for char in plaintext_list:
        if not char.isalpha():
            ciphertext_list.append(char)
        elif char == char.lower():
            alpha_index = alpha_lower.index(char)
            print(alpha_index)
            crypt_char = cipher_list[alpha_index]
            print(crypt_char)
            ciphertext_list.append(crypt_char)
        # if upper-case, want to find better way to do this
        else:
            alpha_index = alpha_lower.index(char.lower())
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char.upper())

    return ciphertext_list
