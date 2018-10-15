# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack = []
        res = []
        while len(stack) != 0 or root:
            while root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                stack.pop()
                if len(res) < k:
                    res.append(root.val)
                elif abs(root.val - target) < abs(res[0] - target):
                    res.pop(0)
                    res.append(root.val)
                else:
                    break
                root = root.right
        return res
