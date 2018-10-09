# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        first = None
        second = None
        prev = None
        stack = []
        curr = root
        while len(stack) != 0 or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev != None and curr.val <= prev.val:
                    if first == None:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
        temp = first.val
        first.val = second.val
        second.val = temp
