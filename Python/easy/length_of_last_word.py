# https://leetcode.com/problems/length-of-last-word/
def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split()[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))

