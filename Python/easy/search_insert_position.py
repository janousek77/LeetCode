from typing import List

# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = int((left+right)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return left 

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))