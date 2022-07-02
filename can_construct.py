from typing import List


def can_construct(target_string: str, components: List[str]) -> bool:
    def check_component(c, i):
        if i + len(c) > len(target_string):
            return False
        for j in range(len(c)):
            if c[j] != target_string[i+j]:
                return False
        return True

    def can_construct_rec(i, memo):
        if i in memo:
            return memo[i]
        if i > len(target_string):
            return False
        if i == len(target_string):
            return True

        for c in components:
            if check_component(c, i) and can_construct_rec(i+len(c), memo):
                memo[i] = True
                return True

        memo[i] = False
        return False

    return can_construct_rec(0, {})


print(can_construct('ab', ['a', 'b']))
