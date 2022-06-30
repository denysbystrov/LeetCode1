"""Number 70: Climbing Stairs"""

"Solving Problem using memoization"
"Key: n, value: number of combinations"


def climb_stairs(n: int) -> int:
    memo = {1: 1, 2: 2}
    count = 3
    while n not in memo:
        memo[count] = memo[count-1] + memo[count-2]
        count += 1

    return memo[n]
