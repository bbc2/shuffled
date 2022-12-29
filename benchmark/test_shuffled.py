from shuffled import Shuffled


def consume_shuffled(n) -> None:
    for _ in Shuffled(n):
        pass


def test_shuffled_performance(benchmark) -> None:
    benchmark(consume_shuffled, 10000)
