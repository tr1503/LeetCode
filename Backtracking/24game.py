# Use backtracking to finish this question.
class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.res = False
        eps = 0.001
        arr = []
        for num in nums:
            arr.append(float(num))
        
        def helper(nums, eps):
            if self.res:
                return
            if len(nums) == 1:
                if abs(nums[0] - 24) < eps:
                    self.res = True
                return
            for i in range(len(nums)):
                for j in range(i):
                    p = nums[i]
                    q = nums[j]
                    expr = [p + q, p - q, q - p, p * q]
                    # Be sure no 0 divide other number
                    if p > eps:
                        expr.append(q / p)
                    if q > eps:
                        expr.append(p / q)
                    # delete the calculated numbers
                    nums.pop(i)
                    nums.pop(j)
                    # calculate them, remember to pop it for backtracking after dfs
                    for e in expr:
                        nums.append(e)
                        helper(nums,eps)
                        nums.pop()
                    #recover the array for backtracking
                    nums.insert(j,q)
                    nums.insert(i,p)
        helper(arr,eps)
        return self.res
