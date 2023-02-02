def affine_encrypt(plaintext_file, ciphertext_file, a, b):
    """

    :param plaintext_file: a *.txt file that will be encrypted
    :param ciphertext_file: the *.txt filename of the returned encrypted file
    :param a: an integer that will be used to encrypt plaintext file
    :param b: an integer that will be used to encrypt plaintext file
    :return:a .txt file that has been encrypted via affine cipher
    """
    if not ab_checker(a,b):
        print("Invalid cipher_alphabet")
        exit()


    cipher_string = affine_alph(a,b) #find the proper cipher string given a, b valid
    cipher = substitution_encrypt(plaintext_file, ciphertext_file, cipher_string)
    return cipher

