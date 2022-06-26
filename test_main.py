from main import add_two_numbers
from main import ListNode

use_cases = (
    ([3, 2, 1], [6, 5, 4]),
    ([8, 7, 5], [6, 2, 1]),
    ([8, 4, 9], [3, 7, 1]),
    ([1, 2, 8, 2], [9, 4, 2, 9, 1, 2, 6, 5]),
    ([8, 4, 3, 2, 5], [5, 3, 1]),
    ([5], [6])
)

use_cases_results = (
    [9, 7, 5],
    [4, 0, 7],
    [1, 2, 1, 1],
    [0, 7, 0, 2, 2, 2, 2, 6, 5],
    [3, 8, 4, 2, 5],
    [1, 1]
)

edge_cases = (
    ([0], [0]),
    ([1, 2, 1, 3], [0]),
    ([9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9])
)

edge_cases_result = (
    [0],
    [1, 2, 1, 3],
    [9, 9, 9, 9, 0, 0, 0, 0, 0, 1]
)


def test_add_two_numbers() -> None:
    assert False
