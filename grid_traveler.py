"""Solution to a grid traveller problem (not on leet code)"""
"Using memoiztion"


def grid_traveller(m: int, n: int, memo={}) -> int:
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1

    key = str(m)+str(n)
    if key not in memo:
        memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)

    return memo[key]


print(grid_traveller(2, 3))
