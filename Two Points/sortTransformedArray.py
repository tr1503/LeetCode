# Use the property of parabola and two points to solve this question
# if a > 0, the left side and right side are larger than the middle
# if a < 0, the middle is larger than the left and right side
# if a == 0, it will become linear so we can put this situation with a > 0
# use two points to put the result from right to left (a >= 0) or left to right (a < 0)
class Solution:
    def cal(self, a, b, c, x):
        return a * x * x + b * x + c
    
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        i = 0
        j = n - 1
        index = 0 if a < 0 else n - 1
        while i <= j:
            if a >= 0:
                if self.cal(a,b,c,nums[i]) >= self.cal(a,b,c,nums[j]):
                    res[index] = self.cal(a,b,c,nums[i])
                    i += 1
                else:
                    res[index] = self.cal(a,b,c,nums[j])
                    j -= 1
                index -= 1
            else:
                if self.cal(a,b,c,nums[i]) >= self.cal(a,b,c,nums[j]):
                    res[index] = self.cal(a,b,c,nums[j])
                    j -= 1
                else:
                    res[index] = self.cal(a,b,c,nums[i])
                    i += 1
                index += 1
        return res
