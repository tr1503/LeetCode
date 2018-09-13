'''Use the divide way from SICP. Dividend - divisor ^ n until it is smaller than divisor.
When dividend is smaller than divisor ^ n, we also need to check from divisor ^ 1 to n more time to get right ans.
Python needs to meet the condition when dividend is smaller than the min integer.'''
class Solution(object):
    def helper(self, dividend, divisor, level):
        if dividend < divisor:
            return 0
        if dividend < divisor * level:
            return self.helper(dividend, divisor, 1)
        else:
            return level + self.helper(dividend - divisor * level, divisor, level * 2)
        
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483648 - 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return self.helper(abs(dividend), abs(divisor), 1)
        else:
            return -(self.helper(abs(dividend), abs(divisor), 1))
