def _crypter(plaintext_list, cipher_list, is_keyword_decrypt=None):
    """
    Uses a pre-defined alphabet list and inputted cipher list to (en/de)crypt the inputted textfile.
    :param plaintext_list: list of characters from plaintext_file
    :param cipher_list: a list of the cipher key
    :param is_keyword_decrypt: optional parameter, takes a boolean value
    :return: a(n) encrypted/decrypted list, ciphertext_list
    """
    ciphertext_list = []
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    # If we are decrypting the keyword cipher, we switch cipher_list and alpha_lower
    if is_keyword_decrypt:
        alpha_lower_copy = alpha_lower
        alpha_lower = cipher_list
        cipher_list = alpha_lower_copy

    for char in plaintext_list:
        # If the character is non-alphabetic, do nothing and append
        if not char.isalpha():
            ciphertext_list.append(char)
        # If lowercase, find corresponding cipher character and append
        elif char == char.lower():
            alpha_index = alpha_lower.index(char)
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char)
        # If uppercase, make char lowercase to find cipher character, then append uppercase cipher character
        else:
            alpha_index = alpha_lower.index(char.lower())
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char.upper())

    return ciphertext_list
