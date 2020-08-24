class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        stack = []
        A = [0] + A + [0]
        for i, num in enumerate(A):
            while stack and A[stack[-1]] > num:
                index = stack.pop()
                k = stack[-1]
                res += A[index] * (i - index) * (index - k)
            stack.append(i)
        return res % (10 ** 9 + 7)
