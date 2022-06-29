import pytest
from square_roor import *

use_cases = (
    (16, 4),
    (8, 2)
)

test_cases = (
    (1, 1),
    (0, 0)
)


@pytest.mark.parametrize(('input_x', 'expected'), use_cases+test_cases)
def test_my_sqrt(input_x, expected):
    assert my_sqrt(input_x) == expected
