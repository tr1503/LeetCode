# total hamming distance = m * n (m is the number of 1, n is the number of 0)
# time is O(n), space is O(1)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count, mask = 0, 1 << i
            for num in nums:
                # count the number of 1
                count += num & mask != 0
            res += count * (len(nums) - count)
        return res
