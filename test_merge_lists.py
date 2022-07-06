import pytest
from merge_lists import merge
from Util import pad_zeros_list


use_cases = (
    ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([4, 6, 9], [1, 2, 10], [1, 2, 4, 6, 9, 10]),
    ([1, 2, 4, 5, 6], [3], [1, 2, 3, 4, 5, 6])
)

edge_cases = (
    ([1], [], [1]),
    ([1, 1, 1], [1, 1, 2], [1, 1, 1, 1, 1, 2])
)


@pytest.mark.parametrize(('nums1', 'nums2', 'expected'), use_cases+edge_cases)
def test_merge(nums1, nums2, expected):
    result = nums1
    n = len(nums1)
    pad_zeros_list(result, len(nums2))
    print(result)
    merge(result, n, nums2, len(nums2))
    assert result == expected
