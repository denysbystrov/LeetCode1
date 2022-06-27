import pytest
import median_two_arrays

use_cases = (
    ([1, 2, 3, 4], [2, 3, 6, 7], 3),
    ([1, 2], [3, 4], 2.5),
    ([1, 4, 5, 6], [2, 3, 7], 4)
)

edge_cases = (
    ([2, 2, 2, 2], [2, 2, 2], 2),
    ([1], [], 1),
    ([], [1], 0)
)


def test_find_median_sorted_arrays():
    assert False
