def list_to_textfile(char_list, textfile_name):
    """
    Converts a list into a textfile.
    :param char_list: list of characters
    :param textfile_name: name of the returned textfile
    :return: a textfile
    """
    # Joining char_list into a string
    joined = ''.join(char_list)
    # Writing a returning textfile with the joined string
    textfile = open(textfile_name, 'w')
    textfile.write(joined)
    textfile.close()

    return textfile
