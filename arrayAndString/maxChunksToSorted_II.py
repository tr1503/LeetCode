class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 1
        n = len(arr)
        forward = arr[:]
        backward = arr[:]
        for i in range(1, n):
            forward[i] = max(arr[i], forward[i - 1])
        for i in range(n-2, -1, -1):
            backward[i] = min(arr[i], backward[i + 1])
        for i in range(n-1):
            if forward[i] <= backward[i+1]:
                res += 1
        return res
