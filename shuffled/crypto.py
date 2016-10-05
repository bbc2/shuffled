from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import math

from . import compat, feistel


class AesRandomizer:
    domain_size = 2 ** 128

    def __init__(self, key):
        self._cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    def randomize(self, integer):
        encoded = compat.int128_to_bytes(integer)
        encryptor = self._cipher.encryptor()
        encrypted = encryptor.update(encoded) + encryptor.finalize()
        return compat.int128_from_bytes(encrypted)


class IndexEncryptor:
    """
    Encrypt indexes using pseudo-random function.

    :param randomizers: List of instances with an appropriate pseudo-random ``randomize``
        method and ``domain_size`` integer attribute,  such as :py:class:`AesRandomizer`
        objects.
    :param size: Size of the domain
    :type size: int
    """
    def __init__(self, randomizers, size):
        if any(size > randomizer.domain_size for randomizer in randomizers):
            raise ValueError('Size too big for at least one of the randomizers')
        self.round_functions = [randomizer.randomize for randomizer in randomizers]
        self.size = size
        self._a = self._b = int(math.ceil(math.sqrt(size)))

    def encrypt(self, index):
        """
        Permutation of ``range(self.size)``

        :param index: Integer in ``range(self.size)``
        :type index: int
        """
        if index < 0 or index >= self.size:
            raise ValueError('Index out of range')
        return feistel.encrypt(self.round_functions, self._a, self._b, index, self.size)
