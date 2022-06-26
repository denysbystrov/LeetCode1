import pytest
from main import *

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
    [0, 7, 0, 2, 2, 2, 6, 5],
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
    [8, 9, 9, 9, 0, 0, 0, 0, 0, 1]
)


def convert_array_to_list(num_array: list) -> ListNode:
    prev_node = None
    start_node = None
    for num in num_array:
        new_node = ListNode(num)
        if prev_node:
            prev_node.next = new_node
        else:
            start_node = new_node
        prev_node = new_node

    return start_node


def convert_list_to_array(node: ListNode) -> list:
    num_array = []
    current_node = node
    while current_node:
        num_array.append(current_node.val)
        current_node = current_node.next

    return num_array


# def test_add_two_numbers() -> None:
#     test_cases = use_cases + edge_cases
#     test_cases_results = use_cases_results + edge_cases_result
#     for i in range(len(test_cases)):
#         l1_array, l2_array = test_cases[i]
#         l1 = convert_array_to_list(l1_array)
#         l2 = convert_array_to_list(l2_array)
#         result_list = add_two_numbers(l1, l2)
#         result_array = convert_list_to_array(result_list)
#         assert result_array == test_cases_results[i]


use_cases_substring = (('abceabcebb', 4),
                       ('abccccccde', 3),
                       ('aaaaaaaa', 1),
                       ('pwwkew', 3))

edge_cases_substring = (('a', 1),
                        ('', 0))


@pytest.mark.parametrize(('input_x', 'expected'), use_cases_substring+edge_cases_substring)
def test_length_of_longest_substring(input_x, expected) -> None:
    assert length_of_longest_substring(input_x) == expected
