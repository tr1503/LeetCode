'''Use dfs iterative way to finish:
Use queue to store the tree node. Use a for loop to dfs all the node at same level.'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        count = 0
        while len(queue) != 0:
            count += 1
            for i in range(len(queue)):
                p = queue[0]
                queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        return count
