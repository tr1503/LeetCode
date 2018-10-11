class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        res = 0
        curr = 0
        maxNext = 0
        for i in range(len(nums)-1):
            maxNext = max(maxNext, nums[i] + i)
            if i == curr:
                res += 1
                curr = maxNext
        return res
