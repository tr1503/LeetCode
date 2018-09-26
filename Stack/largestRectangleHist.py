class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = []
        res = 0
        for i in range(len(heights)):
            #Get possible longest width for largest rectangle
            while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                index = stack.pop()
                if len(stack) == 0:
                    #Only this bar, so width = i
                    temp = i * heights[index]
                else:
                    #width = current bar's position - the last bar in stack for largest rectangle
                    temp = (i - stack[-1] - 1) * heights[index]
                res = max(res,temp)
            stack.append(i)
        
        while len(stack) != 0:
            index = stack.pop()
            if len(stack) == 0:
                #Reach the end, width = overall width
                temp = len(heights) * heights[index]
            else:
                #width = overall width - this reached bar - 1
                temp = (len(heights) - stack[-1] - 1) * heights[index]
            res = max(res,temp)
        return res
