# Shuffled: Random iterators for large integer ranges

Shuffled is a library for iterating randomly and without repetition over integer ranges.
It doesn't store all the integers in memory so that you can work with ranges of up to
2<sup>128</sup> elements, even with your standard RAM available.

```python
>>> shuffled_range = Shuffled(10)
>>> list(shuffled_range)
[4, 1, 2, 9, 8, 5, 3, 0, 6, 7]
>>> same_shuffled_range = Shuffled(10, seed=shuffled_range.seed)
>>> list(same_shuffled_range)
[4, 1, 2, 9, 8, 5, 3, 0, 6, 7]
```

```python
>>> network = ipaddress.IPv4Network('10.0.0.0/8')
>>> shuffled_range = Shuffled(network.num_addresses)
>>> for index in shuffled_range:
...     print(network[index])
...
10.24.41.126
10.67.199.15
10.240.82.199
10.79.219.74
10.166.105.25
10.19.5.91
[...]
```
