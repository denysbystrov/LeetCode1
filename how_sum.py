"""Not a leet code problem. How sum takes in a targetSum and an array of numbers. The function should return an array
of any combination that adds up to targetSum. If there is no such combination is returns null."""


def how_sum(target_sum: int, numbers: list, memo={}):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        val = how_sum(target_sum-num, numbers, memo)
        if val is not None:
            memo[target_sum] = [num] + val
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(how_sum(300, [2, 4]))
