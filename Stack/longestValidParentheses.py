class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        start = -1
        #Use the index to calculate the result by stack
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(res, i - start)
                    else:
                        res = max(res, i - stack[-1])
        return res
