class Solution(object):
    def largestArea(self, height):
        if not height:
            return 0
        res = 0
        stack = []
        for i in range(len(height)):
            while len(stack) != 0 and height[i] <= height[stack[-1]]:
                index = stack.pop()
                if len(stack) == 0:
                    temp = i * height[index]
                else:
                    temp = (i-stack[-1]-1) * height[index]
                res = max(res,temp)
            stack.append(i)
        while len(stack) != 0:
            index = stack.pop()
            if len(stack) == 0:
                temp = len(height) * height[index]
            else:
                temp = (len(height) - stack[-1] - 1) * height[index]
            res = max(res, temp)
        return res
            
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        height = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] = height[j] + 1
            res = max(self.largestArea(height),res)
        return res
