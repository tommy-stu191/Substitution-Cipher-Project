def textfile_to_list(text_file):
    """

    :param text_file: a text file
    :return: a list of characters from the text file
    """
    try:
        open(text_file)
    except FileNotFoundError:
        print("File does not exist.")

    open_file = open(text_file, "r")
    read_file = open_file.read()

    list_file = list(read_file)
    return list_file


textfile_to_list("liquid.txt")

