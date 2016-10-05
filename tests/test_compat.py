import unittest2

from shuffled import compat


class TestCompat(unittest2.TestCase):
    def test_to_bytes(self):
        encoded = b'\x01\x00\x00\x00\x00\x00\x00\x02\x03\x00\x00\x00\x00\x00\x00\x04'
        self.assertEqual(
            encoded,
            compat.int128_to_bytes(0x01000000000000020300000000000004),
        )

    def test_from_bytes(self):
        encoded = b'\x01\x00\x00\x00\x00\x00\x00\x02\x03\x00\x00\x00\x00\x00\x00\x04'
        self.assertEqual(
            0x01000000000000020300000000000004,
            compat.int128_from_bytes(encoded),
        )
