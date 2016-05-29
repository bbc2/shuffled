import hashlib
import os

from . import crypto


class Shuffled:
    def __init__(self, range_size, seed=None):
        self._size = range_size
        if seed is None:
            self.seed = os.urandom(16 * 3)
        else:
            self.seed = seed
        material = hashlib.sha512(self.seed).digest()
        keys = [material[i:i + 16] for i in range(0, 3 * 16, 16)]
        randomizers = [crypto.AesRandomizer(key) for key in keys]
        self.encryptor = crypto.IndexEncryptor(randomizers, range_size)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index not in range(len(self)):
            raise IndexError
        return self.encryptor.encrypt(index)
