# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Use in-order to get kth smallest number
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        count = 0
        while len(stack) != 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right
        return 0
