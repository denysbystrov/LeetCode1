import pytest
from plus_one import *


use_cases = (
    ([1, 2, 3, 4], [1, 2, 3, 5]),
    ([1, 2, 9], [1, 3, 0]),
    ([9, 9], [1, 0, 0])
)

edge_cases = (
    ([1], [2]),
    ([9], [1, 0])
)


@pytest.mark.parametrize(('input_x', 'expected'), use_cases+edge_cases)
def test_plus_one(input_x, expected):
    assert plus_one(input_x) == expected
