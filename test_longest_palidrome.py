import pytest
from longest_palidrome import *

use_cases = (
    ('edfabccbaghgj', 'abccba'),
    ('cbbd', 'bb')
)

edge_cases = (
    ('bbbbbbb', 'bbbbbbb'),
    ('a', 'a')
)


@pytest.mark.parametrize(('input_x', 'expected'), use_cases+edge_cases)
def test_longest_palindrome(input_x, expected):
    assert longest_palindrome(input_x) == expected
