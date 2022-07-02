import pytest
from can_construct import can_construct

use_cases = (
    ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], True),
    ('books', ['boo', 'xvd', 'ooks'], False)
)

edge_cases = (
    ('', ['a', 'abcd', 'edg'], True),
    ('', [], True),
    ('a', ['a'], True),
    ('str', ['strs'], False),
    ('book', ['k', 'o', 'b'], True)
)


@pytest.mark.parametrize(('target_string', 'components', 'expected'), use_cases+edge_cases)
def test_can_construct(target_string, components, expected):
    assert can_construct(target_string, components) == expected
