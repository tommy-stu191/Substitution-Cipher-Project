def atbash_encrypt(plaintext_file, ciphertext_file):
    atbash_alpha = 'zyxwvutsrqponmlkjihgfedcba'
    return substitution_encrypt(plaintext_file, ciphertext_file, atbash_alpha)
