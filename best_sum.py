"""best sum takes in a target sum and an array of numbers. The function should return the array containing the shortest
combination of numbers that add up exactly to target sum. If there is a tie, you can return either."""


def best_sum(target_sum: int, numbers: list, memo={}):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    shortest_array = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers, memo)
        if remainder_result is not None:
            result = [num] + remainder_result
            if shortest_array is None or len(shortest_array) > len(result):
                shortest_array = result

    memo[target_sum] = shortest_array
    return shortest_array


print(best_sum(100, [1, 2, 5, 25]))
