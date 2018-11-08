# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, 0)
    
    def dfs(self, root, val):
        val = val * 10 + root.val
        if (root.left or root.right) is None:
            return val
        sums = 0
        if root.left:
            sums += self.dfs(root.left, val)
        if root.right:
            sums += self.dfs(root.right, val)
        return sums
