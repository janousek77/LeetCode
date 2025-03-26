from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/symmetric-tree/
def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return isSymmetricHelper(root.left, root.right)

def isSymmetricHelper(left, right):
    if not left and not right:
        return True
    if not left and right or left and not right:
        return False
    if left.val != right.val:
        return False
    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)

print(isSymmetric(TreeNode.build_tree_from_array([1,2,2,3,4,4,3]))) # True
print(isSymmetric(TreeNode.build_tree_from_array([1,2,2,None,3,None,3]))) # False