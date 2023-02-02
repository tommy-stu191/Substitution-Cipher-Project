def atbash_encrypt(plaintext_file, ciphertext_file):
    """
    Reverses alphabet and maps new cipher_alphabet to Encrypt based on atbash style
    :param plaintext_file:
    :param ciphertext_file:
    :return:
    """
    atbash_alpha = 'zyxwvutsrqponmlkjihgfedcba'
    return substitution_encrypt(plaintext_file, ciphertext_file, atbash_alpha)
