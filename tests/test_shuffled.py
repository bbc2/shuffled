import unittest2

from shuffled import Shuffled


class TestShuffled(unittest2.TestCase):
    def test_normal(self):
        for i in range(0, 1000, 100):
            with self.subTest(i=i):
                shuffled_range = Shuffled(i)
                self.assertEqual(sorted(list(shuffled_range)), list(range(i)))

    def test_seed(self):
        for seed in (b'', b'\x00', b'\x01'):
            with self.subTest(seed=seed):
                self.assertEqual(list(Shuffled(20, seed)), list(Shuffled(20, seed)))
