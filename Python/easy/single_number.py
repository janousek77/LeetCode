from typing import List, Optional

# https://leetcode.com/problems/single-number/description/
def singleNumber(nums: List[int]) -> int:
    if len(nums) < 2:
        return nums[0]
    
    nums.sort()
    left, right = 0, 1
    while left < len(nums) and right < len(nums):
        if nums[left] != nums[right]:
            if left == 0 or nums[left] != nums[left - 1]:
                return nums[left]
            if right  == len(nums) - 1 or nums[right] != nums[right +1]:
                return nums[right]
        left, right = left+2, right+2
    
    return nums[-1]


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))
