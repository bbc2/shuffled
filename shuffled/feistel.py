def _encrypt(round_functions, a, b, m):
    l = m % a
    r = m // a
    for (j, round_function) in enumerate(round_functions):
        if j % 2 == 0:
            tmp = (l + round_function(r)) % a
        else:
            tmp = (l + round_function(r)) % b
        l = r
        r = tmp

    if len(round_functions) % 2 == 1:
        return a * l + r
    else:
        return a * r + l


def encrypt(round_functions, a, b, m, size):
    ciphertext = m
    while True:
        ciphertext = _encrypt(round_functions, a, b, ciphertext)
        if ciphertext < size:
            return ciphertext
