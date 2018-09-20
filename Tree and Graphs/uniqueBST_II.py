'''Use dfs recursion to get the left tree and right tree separately.'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generate(self, start, end):
        res = []
        if start > end:
            res.append(None)
        for i in range(start, end + 1):
            #Get all left nodes and right nodes
            leftList = self.generate(start, i-1)
            rightList = self.generate(i+1, end)
            for left in leftList:
                for right in rightList:
                    treeNode = TreeNode(i)
                    treeNode.left = left
                    treeNode.right = right
                    res.append(treeNode)
        return res
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)
