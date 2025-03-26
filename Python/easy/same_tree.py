from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/same-tree/
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p and q or p and not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(TreeNode.build_tree_from_array([1,2,3]), TreeNode.build_tree_from_array([1,2,3]))) # True
print(isSameTree(TreeNode.build_tree_from_array([1,2]), TreeNode.build_tree_from_array([1,None,2]))) # False