

def textfile_to_list(text_file):
    """
    Converts .txt to a list of chars
    :param text_file: a text file path
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


def run_generic_substitution_cipher():
    textfile_to_list("liquid.txt")

    return


def main():

    # Insert calls to function that run Generic cipher, keyword cipher, caeser, rot-13...
    return


if __name__ == "__main__":
    main()
