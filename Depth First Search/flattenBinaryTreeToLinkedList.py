# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            dfs(root.left)
            
            root.right = self.prev
            root.left = None
            self.prev = root
        dfs(root)
