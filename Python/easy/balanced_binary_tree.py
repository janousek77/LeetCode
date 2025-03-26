from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/balanced-binary-tree/description/
def isBalanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return isBalanced(root.left) and isBalanced(root.right) and abs(height(root.left) - height(root.right)) <= 1

def height(node: Optional[TreeNode]) -> int:
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

print(isBalanced(TreeNode.build_tree_from_array([3,9,20,None,None,15,7]))) # True
print(isBalanced(TreeNode.build_tree_from_array([1,2,2,3,3,None,None,4,4]))) # False
print('minimum-depth-of-binary-tree'.replace('-', '_'))