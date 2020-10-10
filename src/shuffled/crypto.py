import math
from abc import ABC, abstractmethod, abstractproperty
from typing import Sequence

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from . import feistel


class Randomizer(ABC):
    @abstractproperty
    def domain_size(self) -> int:
        ...

    @abstractmethod
    def randomize(self, integer: int) -> int:
        ...


class AesRandomizer(Randomizer):
    domain_size = 2 ** 128

    def __init__(self, key: bytes) -> None:
        self._cipher = Cipher(
            algorithms.AES(key), modes.ECB(), backend=default_backend()
        )

    def randomize(self, integer: int) -> int:
        encoded = integer.to_bytes(128, byteorder="big")
        encryptor = self._cipher.encryptor()
        encrypted = encryptor.update(encoded) + encryptor.finalize()
        return int.from_bytes(encrypted, byteorder="big")


class IndexEncryptor:
    """
    Encrypt indexes using pseudo-random function.

    :param randomizers: List of instances with an appropriate pseudo-random ``randomize``
        method and ``domain_size`` integer attribute,  such as :py:class:`AesRandomizer`
        objects.
    :param size: Size of the domain
    :type size: int
    """

    def __init__(self, randomizers: Sequence[Randomizer], size: int) -> None:
        if any(size > randomizer.domain_size for randomizer in randomizers):
            raise ValueError("Size too big for at least one of the randomizers")
        self.round_functions = [randomizer.randomize for randomizer in randomizers]
        self.size = size
        self._a = self._b = int(math.ceil(math.sqrt(size)))

    def encrypt(self, index: int) -> int:
        """
        Permutation of ``range(self.size)``

        :param index: Integer in ``range(self.size)``
        :type index: int
        """
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range")
        return feistel.encrypt(self.round_functions, self._a, self._b, index, self.size)
