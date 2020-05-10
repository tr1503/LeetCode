class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def helper(A, K):
            res = 0
            m = {}
            left = 0
            for i in range(len(A)):
                if A[i] not in m:
                    m[A[i]] = 1
                else:
                    m[A[i]] += 1
                while len(m) > K:
                    m[A[left]] -= 1
                    if m[A[left]] == 0:
                        del m[A[left]]
                    left += 1
                res += i - left + 1
            return res
        return helper(A, K) - helper(A, K - 1)
