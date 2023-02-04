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
