from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root