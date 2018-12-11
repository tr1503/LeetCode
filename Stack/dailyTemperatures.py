class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                temp = stack.pop()
                res[temp] = i - temp
            stack.append(i)
        return res
