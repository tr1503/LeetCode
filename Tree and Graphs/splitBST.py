# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        res = [None, None]
        if not root:
            return res
        if root.val <= V:
            res = self.splitBST(root.right,V)
            root.right = res[0]
            #backtracking
            res[0] = root
        else:
            res = self.splitBST(root.left,V)
            root.left = res[1]
            #backtracking
            res[1] = root
        return res
