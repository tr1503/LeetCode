'''Use DFS to convert this question to robber house.
Compare the max number between left and right children + grandparent and add them self to sibling.
rob[0] is max number for passing this house. rob[1] is max number for robbing this house.'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            noRob = left[1] + right[1]
            robCur = max(left[0] + right[0] + root.val, noRob)
            return [noRob, robCur]
        return dfs(root)[1]
