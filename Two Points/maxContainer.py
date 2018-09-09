'''Use two point algorithm to set left point and right point.
Try to get larger width * height.'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, min(height[left],height[right]) * (right - left))
            #Try to get larger height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
