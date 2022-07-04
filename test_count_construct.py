import pytest
from count_construct import count_construct


use_cases = (
    ('abcdef', ['abc', 'ab', 'cd', 'def', 'abcd', 'ef'], 3),
    ('books', ['book', 'oks', 'oo'], 0),
    ('abcd', ['ab', 'abc', 'cd'], 1)
)

edge_cases = (
    ('', ['ab', 'c', 'def'], 1),
    ('a', ['a', 'a', 'a', 'ab'], 3)
)


@pytest.mark.parametrize(('target_string', 'components', 'expected'), use_cases+edge_cases)
def test_count_construct(target_string, components, expected):
    assert count_construct(target_string, components) == expected

