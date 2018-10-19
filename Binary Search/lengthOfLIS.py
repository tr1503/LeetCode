#Use Binary Search to get O(nlogn) solution
#See https://blog.csdn.net/ironyoung/article/details/49664087
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            if len(res) == 0 or res[len(res) - 1] < nums[i]:
                res.append(nums[i])
            else:
                lo = 0
                hi = len(res) - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if res[mid] >= nums[i]:
                        hi = mid
                    else:
                        lo = mid + 1
                res[lo] = nums[i]
        return len(res)
