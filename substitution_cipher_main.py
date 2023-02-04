import math


def cipher_alphabet_checker(cipher_alphabet):
    """
    Checks validity of the cipher_alphabet string.
    :param cipher_alphabet: a string of letters
    :return: a T/F boolean value
    """
    # Converting the string into a list and set for comparison
    cipher_list = cipher_alphabet_to_list(cipher_alphabet)
    cipher_set = set(cipher_list)
    # Using conditionals to test the validity of cipher_alphabet
    if (len(cipher_list) == 26) and\
            (len(cipher_list) == len(cipher_set)) and\
            (cipher_alphabet.isalpha() and
             (cipher_alphabet.islower())):
        return True
    return False


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


def cipher_alphabet_to_list(cipher_alphabet):
    """
    Converts a string into a list.
    :param cipher_alphabet: a string of letters
    :return: a list of letters
    """
    cipher_list = []
    # Appends each character to the list
    for char in cipher_alphabet:
        cipher_list.append(char)

    return cipher_list


def _crypter(plaintext_list, cipher_list, is_keyword_decrypt=None):
    """
    Uses a pre-defined alphabet list and inputted cipher list to (en/de)crypt the inputted textfile.
    :param plaintext_list: list of characters from plaintext_file
    :param cipher_list: a list of the cipher key
    :param is_keyword_decrypt: optional parameter, takes a boolean value
    :return: a(n) encrypted/decrypted list, ciphertext_list
    """
    ciphertext_list = []
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    # If we are decrypting the keyword cipher, we switch cipher_list and alpha_lower
    if is_keyword_decrypt:
        alpha_lower_copy = alpha_lower
        alpha_lower = cipher_list
        cipher_list = alpha_lower_copy

    for char in plaintext_list:
        # If the character is non-alphabetic, do nothing and append
        if not char.isalpha():
            ciphertext_list.append(char)
        # If lowercase, find corresponding cipher character and append
        elif char == char.lower():
            alpha_index = alpha_lower.index(char)
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char)
        # If uppercase, make char lowercase to find cipher character, then append uppercase cipher character
        else:
            alpha_index = alpha_lower.index(char.lower())
            crypt_char = cipher_list[alpha_index]
            ciphertext_list.append(crypt_char.upper())

    return ciphertext_list


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


def shift_cipher(shift: int):
    """
    Shifts the original alphabet list x times
    :param shift: number of shift operations to perform on the cipher list
    :return: a list of encryption
    Ex:
    shift_cipher(3) -> [z,y,x,a,b,c...]
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    shift = shift % 26
    # Removes the last character in the list and places it at the beginning
    for i in range(shift):
        temp = alpha_lower.pop()
        alpha_lower.insert(0, temp)

    return alpha_lower


def a_inverse(a):
    """
    Finds the value of a-inverse.
    :param a: integer parameter for affine cipher
    :return: the inverse of a
    """
    for integer in range(0, 26):
        # Integer is the inverse of a when condition is met
        if a*integer % 26 == 1:
            return integer


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


def affine_alph(a, b):
    """
    Using inputted integers for the Affine Cipher, generates the cipher list and returns it.
    :param a: integer for affine cipher
    :param b: integer for affine cipher
    :return: the affine alphabet for encryption
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    affine_cipher = []
    # Loop until the affine cipher alphabet is full
    while len(affine_cipher) != 26:
        for char in alpha_lower:
            # Find the index of the current character for calculation
            alpha_index = alpha_lower.index(char)
            # Finding and appending the correct letter
            if (a * alpha_index + b) % 26 == count:
                affine_cipher.append(char)
                count += 1
    # Joining the list into a string
    affine_alphabet = ''.join(affine_cipher)

    return affine_alphabet


def affine_alph_decrypt(a, b):
    """
    Using the inverse of parameter a and inputted integers for the Affine Cipher,
    generates the cipher list and returns it.
    :param a: integer for affine cipher
    :param b: integer for affine cipher
    :return: the affine alphabet for encryption
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    affine_cipher = []
    new_a = a_inverse(a)
    # Loop until the affine cipher alphabet is full
    while len(affine_cipher) != 26:
        for char in alpha_lower:
            # Find the index of the current character for calculation
            alpha_index = alpha_lower.index(char)
            # Finding and appending the correct letter
            if new_a*(alpha_index-b) % 26 == count:
                affine_cipher.append(char)
                count += 1
    # Joining the list into a string
    affine_alphabet = ''.join(affine_cipher)

    return affine_alphabet


def keyword_to_cipherlist(keyword):
    """
    Creates a cipher list from a given keyword
    :param keyword: the word being used to encrypt
    :return: cipher_list: list of characters in the alphabet with keyword pulled out to the front for encrypting
    """
    alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    cipher_list = []
    # Take each character from keyword
    for char in keyword:
        lower_char = char.lower()
        # Add the keyword character to the front of cipher list
        cipher_list.append(lower_char)
        alpha_lower.remove(lower_char)
    # Add remaining characters from alpha_lower
    for character in alpha_lower:
        cipher_list.append(character)

    return cipher_list


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


def substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet, is_keyword_decrypt=None):
    """
    Encrypts the given plaintext_file using the substitution method.
    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param cipher_alphabet: a string, the encryption pattern
    :param is_keyword_decrypt: optional parameter, takes a boolean value
    :return: a *.txt file containing the encrypted message
    """

    # Testing validity of cipher_alphabet
    if not cipher_alphabet_checker(cipher_alphabet):
        print("Invalid cipher_alphabet")
        exit()

    # Converting the file & string to lists
    plaintext_list = textfile_to_list(plaintext_file)
    cipher_list = cipher_alphabet_to_list(cipher_alphabet)

    if is_keyword_decrypt:
        ciphertext_list = _crypter(plaintext_list, cipher_list, is_keyword_decrypt=True)
    else:
        ciphertext_list = _crypter(plaintext_list, cipher_list)
    # Converting the list into a textfile
    ciphertext_file = list_to_textfile(ciphertext_list, ciphertext_file)

    return ciphertext_file


def substitution_decrypt(ciphertext_file, plaintext_file, cipher_alphabet):
    """
    Decrypts the given ciphertext_file using the substitution method.
    :param ciphertext_file: The *.txt file being decrypted
    :param plaintext_file: The name of the *.txt file returned
    :param cipher_alphabet: A string "key" for the encryption
    :return: A *.txt plaintext file
    """
    return substitution_encrypt(ciphertext_file, plaintext_file, cipher_alphabet)


def caesar_encrypt(plaintext_file, ciphertext_file, shift: int):
    """
    Encrypts the given plaintext_file using the caesar method with the given shift.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :param shift: an integer, the amount of places to shift
    :return: the encrypted *.txt file
    """
    cipher_list = shift_cipher(shift)
    cipher_alphabet = ''.join(cipher_list)
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)
    return cipher


def caesar_decrypt(ciphertext_file, plaintext_file, shift: int):
    """
    Decrypts the given ciphertext_file using the caesar method with the given shift.
    :param ciphertext_file: the pre-defined encoded *.txt file
    :param plaintext_file: the decoded file to be returned
    :param shift: an integer, the amount of places to shift to the right
    :return: a decoded *.txt file
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, -shift)


def rot13_encrypt(plaintext_file, ciphertext_file):
    """
    Encrypts the given plaintext_file using the ROT-13 method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :return: the encrypted *.txt file
    """
    return caesar_encrypt(plaintext_file, ciphertext_file, 13)


def rot13_decrypt(ciphertext_file, plaintext_file):
    """
    Decrypts the given ciphertext_file using the ROT-13 method.
    :param ciphertext_file: the pre-defined encoded *.txt file
    :param plaintext_file: the decoded file to be returned
    :return: a decoded *.txt file
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, -13)


def atbash_encrypt(plaintext_file, ciphertext_file):
    """
    Encrypts the given plaintext_file using the Atbash method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :return: the encrypted *.txt file
    """
    atbash_alpha = 'zyxwvutsrqponmlkjihgfedcba'
    return substitution_encrypt(plaintext_file, ciphertext_file, atbash_alpha)


def atbash_decrypt(ciphertext_file, plaintext_file):
    """
    Decrypts the given ciphertext_file using the Atbash method.
    :param ciphertext_file: the pre-defined encoded *.txt file
    :param plaintext_file: the decoded file to be returned
    :return: a decoded *.txt file
    """
    return atbash_encrypt(ciphertext_file, plaintext_file)


def keyword_encrypt(plaintext_file, ciphertext_file, keyword, is_keyword_decrypt=None):
    """
    Encrypts the given plaintext_file using the given keyword and the Keyword method.
    :param plaintext_file: the *.txt file to be encrypted
    :param ciphertext_file: the new encrypted *.txt file
    :param keyword: string that defines the cipher
    :param is_keyword_decrypt: optional parameter, takes a boolean value
    :return: the encrypted *.txt file
    """
    # Checking the validity of keyword
    if not keyword_check(keyword):
        print("Invalid keyword")
        exit()

    # Creating the cipher alphabet
    cipher_list = keyword_to_cipherlist(keyword)
    cipher_alphabet = ''.join(cipher_list)

    if is_keyword_decrypt:
        return substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet, is_keyword_decrypt=True)
    else:
        return substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet)


def keyword_decrypt(ciphertext_file, plaintext_file, keyword):
    """
    Decrypts the given ciphertext_file using the given keyword and the Keyword method.
    :param plaintext_file: the new decrypted *.txt file
    :param ciphertext_file: the encrypted *.txt file
    :param keyword: string that defines the cipher
    :return: the decrypted *.txt file
    """
    return keyword_encrypt(ciphertext_file, plaintext_file, keyword, is_keyword_decrypt=True)


def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    """
    Encrypts the given plaintext_file with the parameters a and b using the Affine method.
    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param a: an integer that will be used to encrypt plaintext file
    :param b: an integer that will be used to encrypt plaintext file
    :return:a .txt file that has been encrypted via affine cipher
    """
    if not ab_checker(a):
        print("Invalid cipher_alphabet")
        exit()
    # Find the proper cipher string given a, b valid
    cipher_string = affine_alph(a, b)

    return substitution_encrypt(plaintext_file, ciphertext_file, cipher_string)


def affine_decrypt(ciphertext_file, plaintext_file, a, b):
    """
    Decrypts the given ciphertext_file with the parameters a and b using the Affine method.
    :param ciphertext_file: the *.txt file that will be decrypted
    :param plaintext_file: the *.txt filename of the returned decrypted file
    :param a: an integer that will be used to encrypt plaintext file
    :param b: an integer that will be used to encrypt plaintext file
    :return:a .txt file that has been encrypted via affine cipher
    """
    if not ab_checker(a):
        print("Invalid cipher_alphabet")
        exit()
    # Find the proper cipher string given a, b valid
    cipher_string = affine_alph_decrypt(a, b)

    return substitution_encrypt(ciphertext_file, plaintext_file, cipher_string)
