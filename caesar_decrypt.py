def caesar_decrypt(ciphertext_file, plaintext_file, shift: int):
    """
    Decrypts ciphertext_file using Caesar Cipher, based on shift arg
    :param ciphertext_file: Encrypted .txt file to be decrypted
    :param plaintext_file: Final output of Decryption
    :param shift: Num of shifts to perform decryption
    :return:
    """
    return caesar_encrypt(ciphertext_file, plaintext_file, shift)
