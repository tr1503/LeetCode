class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(s = '', left = 0, right = 0):
            #The length should be 2*n
            if len(s) == 2*n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack()
        return ans
