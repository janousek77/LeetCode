from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/path-sum/description/
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

print(hasPathSum(TreeNode.build_tree_from_array([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22)) # True
print(hasPathSum(TreeNode.build_tree_from_array([1,2,3]), 5)) # False
print(hasPathSum(TreeNode.build_tree_from_array([1,2]), 0)) # False