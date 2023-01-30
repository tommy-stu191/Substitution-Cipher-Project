def list_to_textfile(char_list, textfile_name):
    """

    :param char_list: list of characters
    :param textfile_name: name of the returned textfile
    :return: a textfile
    """
    joined = ''.join(char_list)

    textfile = open(textfile_name, 'w')
    textfile.write(joined)
    textfile.close
    return textfile
