# https://leetcode.com/problems/add-binary/
def addBinary(a: str, b: str) -> str:
    c = int(a,2) + int(b,2)
    return bin(c)[2:]

print(addBinary("11", "1")) # "100"
print(addBinary("1010", "1011")) # "10101"  