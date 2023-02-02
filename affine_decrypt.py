def affine_decrypt(ciphertext_file, plaintext_file, a, b):
    if not ab_checker(a,b):
        print("Invalid cipher_alphabet")
        exit()

    cipher_string = affine_alph_decrypt(a,b)
    cipher = substitution_encrypt(ciphertext_file, plaintext_file, cipher_string)
    return cipher