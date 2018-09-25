class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        #Get its last set bit
        xor &= -xor
        res = [0,0]
        for num in nums:
            #The bit is not set
            if num & xor == 0:
                res[0] ^= num
            #The bit is set
            else:
                res[1] ^= num
        return res
