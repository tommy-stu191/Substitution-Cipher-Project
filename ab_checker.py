import math
def ab_checker(a,b):
    """
    :param a: an integer for affine cipher
    :param b: an integer for affine cipher
    :return: boolean value that determines validity of these integers for use as affine cipher
    """
    if math.gcd(a, 26) == 1:
        return True
    return False



