# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = -float('inf')
        while len(stack) != 0 or root is not None:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= prev:
                    return False
                prev = root.val
                root = root.right
        return True
