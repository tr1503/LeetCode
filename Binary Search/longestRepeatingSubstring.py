class Solution:
    def search(self, L, n, S):
        visited = set()
        for i in range(n - L + 1):
            temp = S[i:i+L]
            if temp in visited:
                return i
            visited.add(temp)
        return -1
    
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(mid, n, S) != -1:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
