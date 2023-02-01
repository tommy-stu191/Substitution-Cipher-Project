import helper_functions
import caesar_cipher


def run_caesar_cipher(shift: int, plain_textfile, cipher_textfile, cipher_alphabet):
    caesar_cipher.caesar_cipher(shift, plain_textfile, cipher_textfile, cipher_alphabet)
    return


def main():
    pre_cipher = [
        "A", "B", "C",
        "D", "E", "F",
        "G", "H", "I",
        "J", "K", "L",
        "M", "N", "O",
        "P", "Q", "R",
        "S", "T", "U",
        "V", "W", "X",
        "Y", "Z"
    ]
    print(helper_functions.shift_cipher(3, pre_cipher))
    # Insert calls to function that run Generic cipher, keyword cipher, caeser, rot-13...
    run_caesar_cipher(3, None, None, pre_cipher)
    return


if __name__ == "__main__":
    main()
