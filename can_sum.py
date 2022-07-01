"""Can sum problem (from youtube video), given a target value and an array of numbers, return true if the target value
can be made by the numbers in the array. Return false if not"""


def can_sum(target_sum: int, numbers: list) -> bool:
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if can_sum(target_sum-num, numbers):
            return True

    return False



