# https://leetcode.com/problems/climbing-stairs/description/
def climbStairs(n: int) -> int:
    if n <= 3:
        return n
    
    prev, prev2, curr = 3, 2, 0
    
    for i in range(3, n):
        curr = prev + prev2
        prev2 = prev
        prev = curr
        
    return curr

print(climbStairs(3)) # 3
print(climbStairs(4)) # 5
print(climbStairs(5)) # 8
print(climbStairs(6)) # 13