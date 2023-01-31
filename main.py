import helper_functions
import substitution_encrypt
import _crypter


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
    # Calls to functions that run Generic cipher, keyword cipher, caeser, rot-13...
    # go here
    substitution_encrypt.substitution_encrypt()



    return


if __name__ == "__main__":
    main()
