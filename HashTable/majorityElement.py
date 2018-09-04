'''Use hash table to store the occurance of each number and find the occurance > n/2. Time complexity is O(n)'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        for num in dict:
            if dict[num] > len(nums) / 2:
                return num
