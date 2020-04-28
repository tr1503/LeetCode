class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        hint = [0] * n
        res = 0
        flip = 0
        
        for i in range(n):
            flip ^= hint[i]
            
            if A[i] == flip:
                res += 1
                if i + K > n:
                    return -1
                flip ^= 1
                if i + K < n:
                    hint[i + K] ^= 1
        return res
