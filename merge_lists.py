"""Number 88: merge two sorted lists"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_queue = []
    index1 = 0
    index2 = 0
    while index1 < m and index2 < n:
        nums1val = nums1[index1] if len(nums1_queue) == 0 else nums1_queue[0]
        nums2val = nums2[index2]
        if nums1val <= nums2val:
            if nums1_queue:
                nums1_queue.pop(0)
            if index2 > 0 and index1+index2 < m:
                nums1_queue.append(nums1[index1+index2])
            nums1[index1+index2] = nums1val
            index1 += 1
        else:
            if index1+index2 < m:
                nums1_queue.append(nums1[index1 + index2])
            nums1[index1 + index2] = nums2val
            index2 += 1

    while index1 < m:
        nums1val = nums1_queue.pop(0) if nums1_queue else nums1[index1]
        if index2 > 0 and index1 + index2 < m:
            nums1_queue.append(nums1[index1 + index2])
        nums1[index1 + index2] = nums1val
        index1 += 1

    while index2 < n:
        nums1[index1 + index2] = nums2[index2]
        index2 += 1


array1 = [1, 2, 4, 5, 6, 0]
merge(array1, 5, [3], 1)
print(array1)
