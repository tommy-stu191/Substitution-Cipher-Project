import helper_functions
import _crypter


def substitution_encrypt(plaintext_file, ciphertext_file, cipher_alphabet):
    """

    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param cipher_alphabet: a string, the encryption pattern
    :return: a *.txt file containing the encrypted message
    """

    # Testing validity of cipher_alphabet
    if not helper_functions.cipher_alphabet_checker(cipher_alphabet):
        print("Invalid cipher_alphabet")
        exit()

    # Converting the file & string to lists
    plaintext_list = helper_functions.textfile_to_list(plaintext_file)
    cipher_list = helper_functions.cipher_alphabet_to_list(cipher_alphabet)

    ciphertext_list = _crypter(plaintext_list, cipher_list)

    ciphertext_file = helper_functions.textfile_to_list(ciphertext_list, ciphertext_file)

    return ciphertext_file
