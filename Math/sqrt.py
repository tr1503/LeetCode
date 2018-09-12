'''Use Newton method: guess = x / 2 and then guess = (guess + x / guess) / 2.0.
From SICP page 14. The times of iter might be smaller.'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        guess = x / 2
        for i in range(100):
            guess = (guess + x / guess) / 2.0
        return int(guess)
