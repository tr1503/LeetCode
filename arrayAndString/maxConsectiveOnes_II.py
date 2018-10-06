'''Set two pointers, one for previous consecutive ones, one for current consecutive ones.
The max consecutive ones after one flip should be previous values + current values.'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr, res = -1, 0, 0
        for num in nums:
            if num == 0:
                prev = curr
                curr = 0
            else:
                curr += 1
            res = max(res, prev + 1 + curr)
        return res
