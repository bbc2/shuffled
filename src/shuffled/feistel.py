from typing import Callable, Sequence


def _encrypt(
    round_functions: Sequence[Callable[[int], int]],
    a: int,
    b: int,
    m: int,
) -> int:
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


def encrypt(
    round_functions: Sequence[Callable[[int], int]],
    a: int,
    b: int,
    m: int,
    size: int,
) -> int:
    """
    Generalized-Feistel encryption

    :param round_functions: List of pseudo-random functions with values in ``range(n)``
                            where ``n >= size``
    :type round_functions: List[int -> int]
    :param a: Positive integer
    :type a: int
    :param b: Positive integer
    :type b: int
    :param m: Message to encrypt in ``range(size)``
    :type m: int
    :param size: Size of the domain
    :type size: int

    The algorithm comes from `Black and Rogaway`_ (Ciphers with Arbitrary Finite Domains,
    2002).

    .. _Black and Rogaway: http://web.cs.ucdavis.edu/~rogaway/papers/subset.pdf
    """
    ciphertext = m
    while True:
        ciphertext = _encrypt(round_functions, a, b, ciphertext)
        if ciphertext < size:
            return ciphertext
