# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''res = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        helper(root)
        return res'''
        if not root:
            return []
        res = []
        stack = [root]
        while len(stack) != 0:
            curr = stack[-1]
            if not curr.left and not curr.right:
                res.append(stack.pop().val)
            else:
                if curr.right:
                    stack.append(curr.right)
                    curr.right = None
                if curr.left:
                    stack.append(curr.left)
                    curr.left = None
        return res
