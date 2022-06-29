import pytest
from maximum_subarray import *

use_cases = (
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 5, 8], 14),
    ([1, -2, -5, 6, -7], 6)
)

edge_cases = (
    ([1], 1),
    ([-1], -1)
)


@pytest.mark.parametrize(('input_x', 'expected'), use_cases+edge_cases)
def test_max_sub_array(input_x, expected):
    assert max_sub_array(input_x) == expected
