import pytest
from can_sum import can_sum

use_cases = (
    (10, [1, 2, 4, 8], True),
    (8, [3, 4, 5, 6], False)
)

edge_cases = (
    (1, [1], True),
    (1, [0], False)
)


@pytest.mark.parametrize(('lhs', 'rhs', 'expected'), use_cases+edge_cases)
def test_can_sum(lhs, rhs, expected):
    assert can_sum(lhs, rhs) == expected
