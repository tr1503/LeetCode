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
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        def helper(root, lst, rest):
            if not root:
                return None
            if not root.left and not root.right:
                if root.val == rest:
                    res.append(lst + [root.val])
            else:
                helper(root.left, lst + [root.val], rest - root.val)
                helper(root.right, lst + [root.val], rest - root.val)
        helper(root,[],sum)
        return res
