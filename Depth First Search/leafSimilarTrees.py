# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        def dfs(root,res):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                dfs(root.left,res)
                dfs(root.right,res)
        dfs(root1,res1)
        dfs(root2,res2)
        return res1 == res2
