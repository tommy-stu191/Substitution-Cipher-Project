def textfile_to_list(text_file):
    """
    Converts a textfile into a list.
    :param text_file: a text file
    :return: a list of characters from the text file
    """
    # Produces an error if no textfile is found
    try:
        open(text_file)
    except FileNotFoundError:
        print("File does not exist.")
    # Opening and reading the textfile
    open_file = open(text_file, "r")
    read_file = open_file.read()
    # Putting the characters of the textfile into a list
    list_file = list(read_file)

    return list_file
