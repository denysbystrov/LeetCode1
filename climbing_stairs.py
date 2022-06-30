"""Number 70: Climbing Stairs"""
import math


def climb_stairs(n: int) -> int:
    num_twos = int(n/2)
    total_ways = 0
    for i in range(1, num_twos+1):
        j = n - 2*i
        combinations = math.factorial(i+j)/(math.factorial(i)*math.factorial(j))
        print(combinations)
        total_ways += combinations

    return total_ways+1
