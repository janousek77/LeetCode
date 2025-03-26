from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    inorder(root, result)
    return result

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)

print(inorderTraversal(TreeNode.build_tree_from_array([1,None,2,3])))