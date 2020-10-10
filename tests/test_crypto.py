import pytest

from shuffled import crypto

KEYS = (
    b"\x00" * 16,
    b"\x01" * 16,
    b"\x02" * 16,
)


class TestEncryptor:
    def test_two_rounds(self):
        randomizers = [crypto.AesRandomizer(key) for key in KEYS[:2]]
        encryptor = crypto.IndexEncryptor(randomizers, 2)
        encryptor.encrypt(0)
        encryptor.encrypt(1)

    def test_three_rounds(self):
        randomizers = [crypto.AesRandomizer(key) for key in KEYS]
        encryptor = crypto.IndexEncryptor(randomizers, 2)
        encryptor.encrypt(0)
        encryptor.encrypt(1)

    def test_out_of_bounds(self):
        randomizers = [crypto.AesRandomizer(key) for key in KEYS]
        encryptor = crypto.IndexEncryptor(randomizers, 2)
        with pytest.raises(ValueError):
            encryptor.encrypt(2)

    def test_size_too_big(self):
        randomizers = [crypto.AesRandomizer(key) for key in KEYS]
        domain_size = randomizers[0].domain_size
        crypto.IndexEncryptor(randomizers, domain_size)
        with pytest.raises(ValueError):
            crypto.IndexEncryptor(randomizers, domain_size + 1)
