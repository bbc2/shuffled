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
        "seed",
        (b"", b"\x00", b"\x01"),
    )
    def test_seed(self, seed):
        assert list(Shuffled(20, seed)) == list(Shuffled(20, seed))
