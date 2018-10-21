# Use binary search #4 kind of usage to solve this question. 
# Use binary search as a function in this question
# check http://www.cnblogs.com/grandyang/p/8627783.html
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[n - 1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            start = 0
            for i in range(n):
                while start < n and nums[i]-nums[start] > mid:
                    start += 1
                count += i - start
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right
