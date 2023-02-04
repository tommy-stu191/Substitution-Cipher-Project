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
