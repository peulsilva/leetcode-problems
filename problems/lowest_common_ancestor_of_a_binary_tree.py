# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p

        while (p.val - root.val) * (q.val - root.val) > 0:
            if p.val > root.val:
                root = root.right
            
            else:
                root = root.left
            
        return root

        
        