# Use the symmerty of matrix and dp to solve this question
# symmerty of matrix can get the number of status manually and mod of number can solve the space TLE
# time is O(n), space is O(1)
class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        mod = 10 ** 9 + 7
        for i in range(N - 1):
            x1, x2, x4, x0 = (x6 + x8) % mod, (x7 + x9) % mod, (x3 + x9 + x0) % mod, (x4 + x6) % mod
            x3, x5, x6, x7, x8, x9 = x1, 0, x4, x1, x2, x1
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % mod
