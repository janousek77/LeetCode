import sys

# https://leetcode.com/problems/roman-to-integer/
def romanToInt(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    previous = 0
    total = 0
    for char in reversed(s):
        if char not in roman:
            return 0
        if roman[char] >= previous:
            total += roman[char]
        else:
            total -= roman[char]
        previous = roman[char]
    return total

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("LVII"))
print(romanToInt("MCMXCIV"))