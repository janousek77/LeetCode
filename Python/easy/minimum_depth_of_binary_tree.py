from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/minimum-depth-of-binary-tree/
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))