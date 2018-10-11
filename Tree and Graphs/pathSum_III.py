# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(root, prev, sum):
            if not root:
                return 0
            curr = prev + root.val
            if curr == sum:
                return 1 + helper(root.left,curr,sum) + helper(root.right,curr,sum)
            else:
                return helper(root.left,curr,sum) + helper(root.right,curr,sum)
        
        if not root:
            return 0
        return helper(root,0,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
