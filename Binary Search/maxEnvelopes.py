class Solution:
    def binarySearch(self, target, nums):
        if not nums:
            return 0
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
    
    def lis(self, nums):
        if not nums:
            return 0
        n = len(nums)
        res = []
        for num in nums:
            pos = self.binarySearch(num, res)
            if pos >= len(res):
                res.append(num)
            else:
                res[pos] = num
        return len(res)
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        if n == 1:
            return 1
        
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        width = []
        for envelope in envelopes:
            width.append(envelope[1])
        res = self.lis(width)
        return res
