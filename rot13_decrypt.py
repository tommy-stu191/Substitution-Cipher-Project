def rot13_decrypt(ciphertext_file, plaintext_file):
    return caesar_encrypt(ciphertext_file, plaintext_file, -13)
