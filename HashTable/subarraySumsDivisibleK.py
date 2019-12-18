class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        arr = [0 for _ in range(K)]
        arr[0] = 1
        s = 0
        res = 0
        for num in A:
            s = (s + num % K + K) % K
            res += arr[s]
            arr[s] += 1
        return res
