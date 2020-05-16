class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1
        
        def helper(L):
            p = pow(26, L, mod)
            curr = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            visited = {curr}
            for i in range(L, len(S)):
                curr = (curr * 26 + A[i] - A[i - L] * p) % mod
                if curr in visited:
                    return i - L + 1
                visited.add(curr)
        res = 0
        left = 0
        right = len(S)
        while left < right:
            mid = (left + right + 1) // 2
            pos = helper(mid)
            if pos:
                left = mid
                res = pos
            else:
                right = mid - 1
        return S[res:res + left]
