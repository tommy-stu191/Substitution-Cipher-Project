def shift_cipher(shift: int):
    """
    Shifts the original alphabet list x times
    :param shift: number of shift operations to perform on the cipher list
    :return: a list of encryption
    Ex:
    shift_cipher(3) -> [z,y,x,a,b,c...]
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    shift = shift % 26
    # Removes the last character in the list and places it at the beginning
    for i in range(shift):
        temp = alpha_lower.pop()
        alpha_lower.insert(0, temp)

    return alpha_lower
