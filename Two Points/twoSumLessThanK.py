class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        
        res = -1
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] < K:
                res = max(res, A[i] + A[j])
                i += 1
            else:
                j -= 1
        return res
