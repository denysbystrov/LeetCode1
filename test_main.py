import pytest
from main import *

use_cases = (
    ([3, 2, 1], [6, 5, 4], [9, 7, 5]),
    ([8, 7, 5], [6, 2, 1], [4, 0, 7]),
    ([8, 4, 9], [3, 7, 1], [1, 2, 1, 1]),
    ([1, 2, 8, 2], [9, 4, 2, 9, 1, 2, 6, 5], [0, 7, 0, 2, 2, 2, 6, 5]),
    ([8, 4, 3, 2, 5], [5, 3, 1], [3, 8, 4, 2, 5]),
    ([5], [6], [1, 1])
)


edge_cases = (
    ([0], [0], [0]),
    ([1, 2, 1, 3], [0], [1, 2, 1, 3]),
    ([9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 0, 0, 1])
)


@pytest.mark.parametrize(('lhs', 'rhs', 'expected'), use_cases+edge_cases)
def test_add_two_numbers(lhs, rhs, expected) -> None:
    l1 = convert_array_to_list(lhs)
    l2 = convert_array_to_list(rhs)
    result_list = add_two_numbers(l1, l2)
    result_array = convert_list_to_array(result_list)
    assert result_array == expected


use_cases_substring = (('abceabcebb', 4),
                       ('abccccccde', 3),
                       ('aaaaaaaa', 1),
                       ('pwwkew', 3),
                       ('dvdf', 3))

edge_cases_substring = (('a', 1),
                        ('', 0))


@pytest.mark.parametrize(('input_x', 'expected'), use_cases_substring+edge_cases_substring)
def test_length_of_longest_substring(input_x, expected) -> None:
    assert length_of_longest_substring(input_x) == expected
