def affine_alph_decrypt(a, b):
    """
    Using the inverse of parameter a and inputted integers for the Affine Cipher,
    generates the cipher list and returns it.
    :param a: integer for affine cipher
    :param b: integer for affine cipher
    :return: the affine alphabet for encryption
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    affine_cipher = []
    new_a = a_inverse(a)
    # Loop until the affine cipher alphabet is full
    while len(affine_cipher) != 26:
        for char in alpha_lower:
            # Find the index of the current character for calculation
            alpha_index = alpha_lower.index(char)
            # Finding and appending the correct letter
            if new_a * (alpha_index - b) % 26 == count:
                affine_cipher.append(char)
                count += 1
    # Joining the list into a string
    affine_alphabet = ''.join(affine_cipher)

    return affine_alphabet
