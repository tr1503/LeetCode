# use greedy algorithm to solve this question, time is O(n^2)
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort(reverse = True)
        n = len(nums)
        res = 0
        for c in range(n - 2):
            b = c + 1
            a = n - 1
            while b < a:
                if nums[a] + nums[b] > nums[c]:
                    res += a - b
                    b += 1
                else:
                    a -= 1
        return res
