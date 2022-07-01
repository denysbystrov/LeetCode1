import pytest

use_cases = (
    (10, [1, 2, 4, 8], True),
    (8, [3, 4, 5, 6], False)
)

edge_cases = (
    (1, [1], True),
    (1, [0], False)
)


def test_can_sum():
    assert False
