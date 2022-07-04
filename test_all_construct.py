import pytest
from Util import check_two_arrays_equivalent
from all_construct import all_construct


use_cases = (
    ('abcdef', ['ab', 'cd', 'ef', 'abcd', 'abc', 'c', 'def'], [['ab', 'cd', 'ef'],
                                                               ['abcd', 'ef'], ['ab', 'c', 'def']]),
    ('books', ['book', 'ook', 'oo', 'boo'], []),
    ('purple', ['pu', 'rp', 'le'], [['pu', 'rp', 'le']])
)

edge_cases = (
    ('', ['ab', 'cd', 'ef'], [[]]),
    ('a', ['a', 'a', 'a', 'ab'], [['a'], ['a'], ['a']])
)


@pytest.mark.parametrize(('target_string', 'word_bank', 'expected'), use_cases+edge_cases)
def test_all_construct(target_string, word_bank, expected):
    result_array = all_construct(target_string, word_bank)
    print(result_array)
    assert check_two_arrays_equivalent(result_array, expected)
