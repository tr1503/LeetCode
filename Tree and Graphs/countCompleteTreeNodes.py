# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        hLeft = 0
        hRight = 0
        left = root
        right = root
        while left:
            hLeft += 1
            left = left.left
        while right:
            hRight += 1
            right = right.right
        if hLeft == hRight:
            return 2 ** hLeft - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
