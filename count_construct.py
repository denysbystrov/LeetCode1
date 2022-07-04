"""Count construct, takes sting and array of strings. Returns the total number of ways the target string can be made
up from the component strings"""
from typing import List


def count_construct(target_sring: str, word_bank: List[str]) -> int:
    memo = {}

    def word_is_prefix(word, i):
        if len(word) + i > len(target_sring):
            return False

        for j in range(0, len(word)):
            if word[j] != target_sring[i+j]:
                return False
        return True

    def count_construct_rec(i):
        if i in memo:
            return memo[i]
        if i == len(target_sring):
            return 1
        if i > len(target_sring):
            return 0

        total = 0
        for w in word_bank:
            if word_is_prefix(w, i):
                total += count_construct_rec(i+len(w))

        memo[i] = total
        return total

    return count_construct_rec(0)


