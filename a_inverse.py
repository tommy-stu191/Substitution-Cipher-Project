def a_inverse(a):
    """
    Finds the value of a-inverse.
    :param a: integer parameter for affine cipher
    :return: the inverse of a
    """
    for integer in range(0, 26):
        # Integer is the inverse of a when condition is met
        if a*integer % 26 == 1:
            return integer
