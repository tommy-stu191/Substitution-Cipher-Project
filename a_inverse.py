
def affine_alph(a,b):
    """

    :param a: integer for affine cipher
    :param b: integer for affine cipher
    :return: the affine alphabet for encryption
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    affine_cipher = []

    while len(affine_cipher) != 26: # loop until the affine cipher alphabet is full
        for char in alpha_lower:
            alpha_index = alpha_lower.index(char) # find the index of the current character for calculation
            if (a*alpha_index+b)%26 == count: # to ensure the cipher
                affine_cipher.append(char)
                count += 1
    affine_alphabet = ''.join(affine_cipher)
    return affine_alphabet


print(affine_alph(9,7))



