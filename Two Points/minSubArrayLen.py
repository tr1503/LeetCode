class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        '''
        Use two points O(n)
        res = float('inf')
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while left <= i and sum >= s:
                res = min(res,i - left + 1)
                sum -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return res
        '''
        
        #Use binary search O(nlogn)
        n = len(nums)
        sums = [0] * (n + 1)
        res = n + 1
        for i in range(1,n+1):
            sums[i] = sums[i-1] + nums[i-1]
        for i in range(n+1):
            right = self.searchRight(i+1, n, sums[i]+s, sums)
            if right == n + 1:
                break
            if res > right - i:
                res = right - i
        if res == n + 1:
            return 0
        return res
    
    def searchRight(self, left, right, key, sums):
        while left <= right:
            mid = (left + right) / 2
            if sums[mid] >= key:
                right = mid - 1
            else:
                left = mid + 1
        return left
