"""Number 88: merge two sorted lists"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    index1 = m-1
    index2 = n-1
    while index1 >= 0 and index2 >= 0:
        if nums1[index1] >= nums2[index2]:
            nums1[index1 + index2 + 1] = nums1[index1]
            index1 -= 1
        else:
            nums1[index1 + index2 + 1] = nums2[index2]
            index2 -= 1

    while index2 >= 0:
        nums1[index1 + index2 + 1] = nums2[index2]
        index2 -= 1


array1 = [4, 6, 9, 0, 0, 0]
merge(array1, 3, [1, 2, 10], 3)


