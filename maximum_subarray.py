"""Number 53: Maximum Subarray"""


def max_sub_array(nums: list) -> int:
    max_totals = [nums[0]]
    for i in range(1, len(nums)):
        if max_totals[i-1] < 0:
            max_totals.append(nums[i])
        else:
            max_totals.append(max_totals[i-1]+nums[i])

    return max(max_totals)
