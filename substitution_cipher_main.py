def cipher_alphabet_checker(cipher_alphabet: str):
    """
    Checks that cipher alphabet given, meet specifications:
    1. 26 Chars
    2. No duplicates
    3. ...
    :param cipher_alphabet: a string of letters
    :return: a T/F boolean value
    """

    cipher_list = cipher_alphabet_to_list(cipher_alphabet)
    cipher_set = set(cipher_list)

    if (len(cipher_list) == 26) and\
            (len(cipher_list) == len(cipher_set)) and\
            (cipher_alphabet.isalpha() and
             (cipher_alphabet.islower())):
        return True
    return False


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


def cipher_alphabet_to_list(cipher_alphabet):
    """

    :param cipher_alphabet: a string of letters
    :return: a list of letters
    """
    cipher_list = []

    for char in cipher_alphabet:
        cipher_list.append(char)
    return cipher_list


def _crypter(plaintext_list, cipher_list):
    """

    :param plaintext_list: list of characters from plaintext_file
    :param cipher_list: a list of the cipher key
    :return: a(n) encrypted/decrypted list, ciphertext_list
    """
    ciphertext_list = []
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    for char in plaintext_list:
        if not char.isalpha():
            ciphertext_list.append(char)
        elif char == char.lower():
            alpha_index = alpha_lower.index(char)
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char)
        # if upper-case, want to find better way to do this
        else:
            alpha_index = alpha_lower.index(char.lower())
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char.upper())

    return ciphertext_list


def list_to_textfile(char_list, textfile_name):
    """

    :param char_list: list of characters
    :param textfile_name: name of the returned textfile
    :return: a textfile
    """
    joined = ''.join(char_list)

    textfile = open(textfile_name, 'w')
    textfile.write(joined)
    textfile.close()
    return textfile


def shift_cipher(shift: int):
    """
    Shifts the original alphabet list x times
    :param shift: number of shift operations to perform on the cipher list
    :param pre_cipher: list containing all chars to be encrypted
    :return: list of encryption
    Ex:
    shift_cipher(3,[a..z]) -> [z,y,x,a,b,c...]
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    shift = shift % 26
    for i in range(shift):
        temp = alpha_lower.pop()
        alpha_lower.insert(0, temp)
    return alpha_lower


def substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet):
    """
    Encrypts the plaintext_file based on generic substitution encyrption
    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param cipher_alphabet: a string, the encryption pattern
    :return: a *.txt file containing the encrypted message
    """

    # Testing validity of cipher_alphabet
    if not cipher_alphabet_checker(cipher_alphabet):
        print("Invalid cipher_alphabet")
        exit()

    # Converting the file & string to lists
    plaintext_list = textfile_to_list(plaintext_file)
    cipher_list = cipher_alphabet_to_list(cipher_alphabet)

    ciphertext_list = _crypter(plaintext_list, cipher_list)

    ciphertext_file = list_to_textfile(ciphertext_list, ciphertext_file)

    return ciphertext_file


def substitution_decrypt(ciphertext_file, plaintext_file, cipher_alphabet):
    """

    :param ciphertext_file: The *.txt file being decrypted
    :param plaintext_file: The name of the *.txt file returned
    :param cipher_alphabet: A string "key" for the encryption
    :return: A *.txt plaintext file
    """
    return substitution_encrypt(ciphertext_file, plaintext_file, cipher_alphabet)


def caesar_encrypt(plaintext_file, ciphertext_file, shift: int):
    cipher_list = shift_cipher(shift)
    cipher_alphabet = ''.join(cipher_list)
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
    return cipher


def caesar_decrypt(ciphertext_file, plaintext_file, shift: int):
    return caesar_encrypt(ciphertext_file, plaintext_file, shift)


def rot13_encrypt(plaintext_file, ciphertext_file):
    return caesar_encrypt(plaintext_file, ciphertext_file, 13)


def rot13_decrypt(ciphertext_file, plaintext_file):
    return caesar_encrypt(ciphertext_file, plaintext_file, -13)


def atbash_encrypt(plaintext_file, ciphertext_file):
    atbash_alpha = 'zyxwvutsrqponmlkjihgfedcba'
    return substitution_encrypt(plaintext_file, ciphertext_file, atbash_alpha)


def atbash_decrypt(ciphertext_file, plaintext_file):
    return atbash_encrypt(ciphertext_file, plaintext_file)
