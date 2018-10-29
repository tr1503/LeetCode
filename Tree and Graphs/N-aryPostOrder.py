"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if root:
                for child in root.children:
                    helper(child)
                res.append(root.val)
        helper(root)
        return res
