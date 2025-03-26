from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1+ max(maxDepth(root.left), maxDepth(root.right))

print(maxDepth(TreeNode.build_tree_from_array([3,9,20,None,None,15,7])))
print(maxDepth(TreeNode.build_tree_from_array([1,None,2])))