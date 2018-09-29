'''Set two pointers from left side and right side. 
When the current value is same as last value, do nothing.
If right value is same as current value, right = i - 1.
If right value is different from current value, the result should be changed to the max value
between current result and the sliding window from left to this position of current new value.
And left = right + 1 to keep the sliding window. The result should be max value between the 
length of right part and the length of sliding window.'''
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = -1
        res = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                continue
            if right >= 0 and s[right] != s[i]:
                res = max(res, i - left)
                left = right + 1
            right = i - 1
        return max(len(s) - left, res)
