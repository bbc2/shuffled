import hashlib
import os

from . import crypto


class Shuffled:
    """
    Randomized integer ranges

    :param range_size: Size of the range
    :type range_size: int
    :param seed: Seed to make randomization repeatable
    :type seed: bytes

    >>> shuffled_range = Shuffled(10)
    >>> list(shuffled_range)
    [4, 1, 2, 9, 8, 5, 3, 0, 6, 7]
    >>> same_shuffled_range = Shuffled(10, seed=shuffled_range.seed)
    >>> list(same_shuffled_range)
    [4, 1, 2, 9, 8, 5, 3, 0, 6, 7]
    """

    def __init__(self, range_size, seed=None):
        self._size = range_size

        if seed is None:
            self._seed = os.urandom(16 * 3)
        else:
            self._seed = seed
        material = hashlib.sha512(self.seed).digest()
        keys = [material[i:i + 16] for i in range(0, 3 * 16, 16)]
        randomizers = [crypto.AesRandomizer(key) for key in keys]
        self._encryptor = crypto.IndexEncryptor(randomizers, range_size)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError
        return self._encryptor.encrypt(index)

    @property
    def seed(self):
        """
        Seed of the randomization.

        It can be used to create a new identical :py:class:`Shuffled` object.
        """
        return self._seed
