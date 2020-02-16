import struct


def int128_to_bytes(integer):
    low = integer & 0xffffffffffffffff
    high = integer >> 64
    return struct.pack('>QQ', high, low)


def int128_from_bytes(encoded):
    (high, low) = struct.unpack('>QQ', encoded)
    return (high << 64) + low
