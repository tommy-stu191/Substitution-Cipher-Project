def a_inverse(a):
    for int in range(0, 26):
        if a*int % 26 == 1:
            return int


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

    for char in alpha_lower:
        alpha_index = alpha_lower.index(char)
        print(count)
        print((a*alpha_index+b)%26) #grab the index of the current letter being checked
        if (a*alpha_index+b)%26 == count:
            affine_cipher = affine_cipher.append(char)
            print(affine_cipher)
            alpha_lower.remove(char)
            count += 1


print(affine_alph(3,7))



