import pytest

from shuffled import Shuffled


class TestShuffled:
    @pytest.mark.parametrize(
        "range_size",
        range(0, 1000, 100),
    )
    def test_normal(self, range_size):
        shuffled_range = Shuffled(range_size)
        assert sorted(list(shuffled_range)) == list(range(range_size))

    @pytest.mark.parametrize(
        "seed, expected",
        (
            (
                b"",
                [4, 5, 6, 1, 2, 7, 8, 3, 10, 11, 13, 9, 16, 17, 12, 15, 18, 19, 14, 0],
            ),
            (
                b"\x00",
                [13, 14, 17, 7, 3, 15, 16, 6, 2, 5, 9, 12, 18, 10, 1, 19, 4, 0, 8, 11],
            ),
            (
                b"\x01",
                [11, 0, 9, 5, 6, 10, 19, 4, 13, 14, 8, 16, 17, 18, 15, 12, 1, 2, 7, 3],
            ),
        ),
    )
    def test_seed(self, seed, expected):
        assert list(Shuffled(20, seed)) == expected

    def test_negative_index(self):
        s = Shuffled(10, seed=b"\x00")

        assert s[-1] == s[9]
        assert s[-10] == s[0]

    def test_negative_index_out_of_bounds(self):
        s = Shuffled(10, seed=b"\x00")

        with pytest.raises(IndexError):
            s[-11]
