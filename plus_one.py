

def plus_one(digits: list) -> list:
    addition_carry = 1
    idx = len(digits)-1
    while addition_carry > 0 and idx >= 0:
        s = digits[idx] + addition_carry
        new_digit = s % 10
        addition_carry = int(s / 10)
        digits[idx] = new_digit
        idx = idx-1

    if addition_carry == 1:
        digits.insert(0, 1)

    return digits