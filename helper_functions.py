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


def cipher_alphabet_to_list(string):
    """

    :param string:
    :return:
    """
    cipher_list = []
    for char in string:
        cipher_list.append(char)
    return cipher_list


def cipher_alphabet_checker(cipher_alphabet, cipher_alphabet_list):
    """

    :param cipher_alphabet: a string of letters
    :param cipher_alphabet_list: a list of cipher_alphabet
    :return: a boolean value
    """

    cipher_alphabet_set = set(cipher_alphabet_list)

    if (len(cipher_alphabet_list) == 26) \
            and (len(cipher_alphabet_list) == len(cipher_alphabet_set)) \
            and (cipher_alphabet.isalpha()):
        return True
    return False


def shift_cipher(shift: int, pre_cipher: list):
    """
    Shifts the original alphabet list x times
    :param shift: number of shift operations to perform on the cipher list
    :param pre_cipher: list containing all chars to be encrypted
    :return: list of encryption
    Ex:
    shift_cipher(3,[a..z]) -> [z,y,x,a,b,c...]
    """
    shift = shift % 26
    for i in range(shift):
        temp = pre_cipher.pop()
        pre_cipher.insert(0, temp)
    return pre_cipher





