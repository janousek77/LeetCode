from typing import List

# https://leetcode.com/problems/plus-one/description/
def plusOne(digits: List[int]) -> List[int]:
    i = len(digits) - 1
    while i < len(digits) and i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        i -= 1
    return [1] + digits

print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9, 9]))

    