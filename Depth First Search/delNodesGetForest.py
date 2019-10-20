# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        s = set(to_delete)
        def helper(n):
            if not n:
                return None
            n.left = helper(n.left)
            n.right = helper(n.right)
            if n.val not in s:
                return n
            if n.left:
                res.append(n.left)
            if n.right:
                res.append(n.right)
            return None
        
        root = helper(root)
        if root:
            res.append(root)
        return res
