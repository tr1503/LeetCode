class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        trap = 0
        
        #Get the left bars' max value for each bar, from left to right
        for i in range(1,n):
            left[i] = max(left[i-1],height[i-1])
        #Get the right bars' max value for each bar, from right to left
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i+1])
        #Iter all bars, the trapped value for each bar should be min value between left bar - current bar's value
        #and right bar - current bar's value. And get the sum of trap.
        for i in range(n):
            m = min(left[i],right[i])
            if m - height[i] > 0:
                trap += m - height[i]
        return trap
