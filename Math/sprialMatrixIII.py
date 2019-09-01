# One step and one step to finish spiral matrix to solve this problem
# time is O(max(R,C) ^ 2), space is O(R*C)
class Solution:
    def spiralMatrixIII(self, R: int, C: int, x: int, y: int) -> List[List[int]]:
        res = []
        dx, dy, n = 0, 1, 0
        while len(res) < R * C:
            for i in range(int(n / 2 + 1)):
                if x >= 0 and x < R and y >= 0 and y < C:
                    res.append([x, y])
                x, y = x + dx, y + dy
            dx, dy, n = dy, -dx, n + 1
        return res
