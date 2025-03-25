# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))