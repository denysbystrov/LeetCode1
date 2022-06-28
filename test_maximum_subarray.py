import pytest

use_cases = (
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 5, 8], 14),
    ([1, -2, -5, 6, -7], 6)
)

edge_cases = (
    ([1], 1),
    ([-1], -1)
)


def test_max_sub_array():
    assert False
