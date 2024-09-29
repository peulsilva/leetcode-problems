# Definition for a binary tree node.

# https://leetcode.com/problems/path-sum-ii/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

from copy import deepcopy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def is_leaf(root):
            return (root.left is None) and (root.right is None)

        def search(root, target, path):
            if root == None:
                return []

            if is_leaf(root):
                if target - root.val == 0:
                    path.append(root.val)
                    if isinstance(path[0], int):
                        return [path]
                    return path

                else:
                    return []
            
            path.append(root.val)
            left = search(root.left, target - root.val, deepcopy(path))
            right = search(root.right, target - root.val, deepcopy(path))
            # path.pop()

            ans = []
            if len(left) != 0 :
                if isinstance(left[0], list):
                    for el in left: ans.append(el)

                elif isinstance(left[0], int):
                    ans.append(left)

            if len(right)!=0:
                if isinstance(right[0], list):
                    for el in right: ans.append(el)

                elif isinstance(right[0], int):
                    ans.append(right)
                
            return ans

        return search(root, targetSum, [])