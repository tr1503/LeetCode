# Use sliding window to set the flag and get the current length of CIS
# similar with question 3
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = flag = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                flag = i
            res = max(res, i - flag + 1)
        return res
