class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        m = set(nums)
        
        for num in m:
            streak = 0
            #Use hashmap to avoid the repeated check
            if num - 1 not in m:
                curr = num
                streak = 1
                while curr + 1 in m:
                    curr += 1
                    streak += 1
            res = max(res,streak)
            
        return res
