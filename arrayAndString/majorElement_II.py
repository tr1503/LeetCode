'''Use Boyer-Moore Majority Vote algorithm to set two candidates and two counts. 
After first loop, need to have a second loop to check if it appears more than n/3 by using list.count().
Time Complexity is linear and space is O(1). Check https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count_one = 0
        count_two = 0
        candidate_one = 0
        candidate_two = 0
        for num in nums:
            if candidate_one == num:
                count_one += 1
            elif candidate_two == num:
                count_two += 1
            elif count_one == 0:
                candidate_one = num
                count_one += 1
            elif count_two == 0:
                candidate_two = num
                count_two += 1
            else:
                count_one -= 1
                count_two -= 1
        result = []
        if candidate_one == candidate_two and nums.count(candidate_one) > len(nums)/3:
            result.append(candidate_one)
        else:
            for value in (candidate_one, candidate_two):
                if nums.count(value) > len(nums) / 3:
                    result.append(value)
        return result
