class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Hash map way, time: O(n+n), space: O(n)
        '''m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        for key in m:
            if m[key] == 1:
                return key'''
        #Bit Manipulation
        '''a xor a = 0 and a xor 0 = a
        So finally we can get the single number.
        Time: O(n), space: O(1)'''
        res = 0
        for num in nums:
            res ^= num
        return res
