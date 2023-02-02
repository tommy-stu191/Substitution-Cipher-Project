def a_inverse(a):
    for int in range(0, 26):
        if a*int % 26 == 1:
            return int


print(a_inverse(15))

