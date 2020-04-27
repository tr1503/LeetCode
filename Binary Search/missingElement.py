class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(i):
            return nums[i] - nums[0] - i
        
        l = 0
        h = len(nums)
        
        while l < h:
            mid = (l + h) // 2
            if missing(mid) < k:
                l = mid + 1
            else:
                h = mid
        
        return nums[l-1] + k - missing(l - 1)
