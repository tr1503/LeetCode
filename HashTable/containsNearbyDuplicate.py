class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = i
            else:
                if i - m[nums[i]] <= k:
                    return True
                m[nums[i]] = i
        return False
