# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root):
        stack = []
        res = []
        while len(stack) != 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                res.append(None)
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
    
    def preorder(self,root):
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
            else:
                res.append(None)
        res = []
        helper(root)
        return res
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.inorder(p) == self.inorder(q) and self.preorder(p) == self.preorder(q)
