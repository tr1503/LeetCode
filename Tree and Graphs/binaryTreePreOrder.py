# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''res = []
        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return res'''
        
        if not root:
            return []
        res = []
        stack = [root]
        while len(stack) != 0:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res
