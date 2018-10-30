class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(start, end):
            if start == end:
                return nums[start]
            
            mid = (end-start) // 2 - start
            left = helper(start,mid)
            right = helper(mid + 1,end)
            
            if left == right:
                return left
            else:
                left_count = 0
                right_count = 0
                for i in range(start, end + 1):
                    if nums[i] == left:
                        left_count += 1
                for i in range(start, end + 1):
                    if nums[i] == right:
                        right_count += 1
                return left if left_count > right_count else right
        
        return helper(0, len(nums) - 1)
