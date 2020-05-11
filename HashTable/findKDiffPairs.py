class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        m = collections.Counter(nums)
        for num in set(nums):
            if k > 0 and num + k in m:
                res += 1
            if k == 0 and m[num] > 1:
                res += 1
        return res
