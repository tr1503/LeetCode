# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #Use recursion with two values: one for the current max length,
        #One for the last number to check consecutive sequence
        def search(root, length, prev):
            if not root:
                return length
            if prev + 1 == root.val:
                currLen = length + 1
            else:
                currLen = 1
            return max(currLen, max(search(root.left, currLen, root.val), search(root.right, currLen, root.val)))
        return search(root,0,root.val - 1)
