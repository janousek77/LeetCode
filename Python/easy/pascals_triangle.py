from Python.TreeNode import TreeNode
from typing import List, Optional

# https://leetcode.com/problems/pascals-triangle/description/
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    result = [[1]]
    for i in range(1, numRows):
        result.append([1] + [result[i-1][j] + result[i-1][j+1] for j in range(len(result[i-1])-1)] + [1])
    return result