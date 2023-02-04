def ab_checker(a):
    """
    The parameter a must be co-prime with 26
    :param a: an integer for affine cipher
    :return: boolean value that determines validity of these integers for use as affine cipher
    """
    # Checking the validity of parameter a
    if math.gcd(a, 26) == 1:
        return True

    return False
