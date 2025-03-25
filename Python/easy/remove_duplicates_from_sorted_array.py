from typing import List

def removeDuplicates(nums: List[int]) -> int:
    my_set = set()
    i = 0
    while i < len(nums):
        if nums[i] not in my_set:
            my_set.add(nums[i])
            i += 1
        else:
            nums.remove(nums[i])

    return len(nums)

print(removeDuplicates([1,1,2]))  # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # 5