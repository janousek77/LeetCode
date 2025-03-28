# https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ')' and stack[-1] != '(':
                return False
            if c == ']' and stack[-1] != '[':
                return False
            if c == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("[]"))