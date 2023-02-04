def keyword_to_cipherlist(keyword):
    """
    Creates a cipher list from a given keyword
    :param keyword: the word being used to encrypt
    :return: cipher_list: list of characters in the alphabet with keyword pulled out to the front for encrypting
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    cipher_list = []
    # Take each character from keyword
    for char in keyword:
        lower_char = char.lower()
        # Add the keyword character to the front of cipher list
        cipher_list.append(lower_char)
        alpha_lower.remove(lower_char)
    # Add remaining characters from alpha_lower
    for character in alpha_lower:
        cipher_list.append(character)

    return cipher_list