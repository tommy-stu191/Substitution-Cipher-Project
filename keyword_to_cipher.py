def keyword_to_cipherlist(keyword):
    """
    :param keyword: the word being used to encrypt
    :return: cipher_list: list of characters in the alphabet with keyword pulled out to the front for encrypting
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    cipher_list = []
    for char in keyword:  # take each character from keyword
        lower_char = char.lower() # make it lowercase to match alpha list
        cipher_list.append(lower_char) #add the keyword characters to the front of cipherlist
        alpha_lower.remove(lower_char)
    for character in alpha_lower:
        cipher_list.append(character) #add remaining characters from alpha_lower

    return cipher_list

print(keyword_to_cipherlist('second'))
