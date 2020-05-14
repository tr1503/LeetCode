# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val and node.val <= R:
                    res += node.val 
                if L < node.val:
                    stack.append(node.left)
                if R > node.val:
                    stack.append(node.right)
        return res
