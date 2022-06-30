import pytest
from climbing_stairs import *


use_cases = (
    (3, 3),
    (4, 5)
)

edge_cases = (
    (1, 1),
    (2, 2)
)


@pytest.mark.parametrize(('input_x', 'expected'), use_cases+edge_cases)
def test_climb_stairs(input_x, expected):
    assert climb_stairs(input_x) == expected
