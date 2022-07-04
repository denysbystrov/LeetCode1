"""All construct. Write a function that takes a target string and an array of strings. The function returns a 2D
array of all the ways that the target string can be made"""
from typing import List


def all_construct(target_string: str, word_bank: List[str]) -> List:

    memo = {}

    def add_word_to_array(array: List, w: str) -> None:
        for i in range(len(array)):
            array[i].append(w)

    def word_is_prefix(word, i):
        if len(word) + i > len(target_string):
            return False

        for j in range(0, len(word)):
            if word[j] != target_string[i + j]:
                return False
        return True

    def count_construct_rec(i):
        if i in memo:
            return memo[i]
        if i == len(target_string):
            return [[]]
        if i > len(target_string):
            return None

        return_array = []
        for w in word_bank:
            if word_is_prefix(w, i):
                previous_array = count_construct_rec(i + len(w))
                if previous_array is not None and previous_array != []:
                    add_word_to_array(previous_array, w)
                    return_array += previous_array

        memo[i] = return_array
        return return_array

    return count_construct_rec(0)


print(all_construct('purple', ['pu', 'rp', 'le']))
