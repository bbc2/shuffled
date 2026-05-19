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
        subject = Shuffled(10, seed=b"\x00")
        assert subject[-1] == subject[9]
        assert subject[-10] == subject[0]

    def test_negative_index_out_of_bounds(self):
        subject = Shuffled(10, seed=b"\x00")

        with pytest.raises(IndexError):
            subject[-11]

    def test_slice(self):
        subject = Shuffled(10)
        ref = list(subject)
        assert subject[2:5] == ref[2:5]
        assert subject[:3] == ref[:3]
        assert subject[7:] == ref[7:]
        assert subject[::2] == ref[::2]
        assert subject[-3:] == ref[-3:]
        assert subject[1:-1] == ref[1:-1]
        assert subject[5:2:-1] == ref[5:2:-1]
        assert subject[20:30] == ref[20:30]
