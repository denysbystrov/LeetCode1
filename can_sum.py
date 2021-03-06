"""Can sum problem (from youtube video), given a target value and an array of numbers, return true if the target value
can be made by the numbers in the array. Return false if not"""


def can_sum(target_sum: int, numbers: list, memo={}) -> bool:
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        if can_sum(target_sum-num, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False

