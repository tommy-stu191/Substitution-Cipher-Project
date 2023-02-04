def keyword_check(keyword):
    """
    Checks the validity of the inputted keyword
    :param keyword: string that defines the cipher
    :return: a boolean value
    """
    # Creates a list and a set from the keyword string
    keyword_list = cipher_alphabet_to_list(keyword)
    keyword_set = set(keyword_list)
    # If they are the same length, there are no duplicates
    if len(keyword_list) == len(keyword_set):
        return True

    return False
