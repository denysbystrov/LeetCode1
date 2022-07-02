"""Not a leet code problem. How sum takes in a targetSum and an array of numbers. The function should return an array
of any combination that adds up to targetSum. If there is no such combination is returns null."""


def how_sum(target_sum: int, numbers: list):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        val = how_sum(target_sum-num, numbers)
        if val is not None:
            return [num] + val

    return None


print(how_sum(7, [2, 4]))
