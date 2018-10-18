# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = [(root,"")]
        res = []
        if not root:
            return res
        while stack:
            t = stack.pop()
            node = t[0]
            strr = t[1]
            if not node.left and not node.right:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left,strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right,strr + str(node.val) + "->"))
        return res
