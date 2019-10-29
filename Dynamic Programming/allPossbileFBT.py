# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        dp = [[] for _ in range(N + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, N + 1, 2):
            for j in range(1, i, 2):
                k = i - j - 1
                for l in dp[j]:
                    for r in dp[k]:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        dp[i].append(root)
        return dp[N]
