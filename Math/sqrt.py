'''Use Newton method: guess = x / 2 and then guess = (guess + x / guess) / 2.0.
From SICP page 14. The times of iter might be smaller.'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Newton method:
        if x == 0 or x == 1:
            return x
        guess = x / 2
        for i in range(19):
            guess = (guess + x / guess) / 2.0
        return int(guess)
        #Binary Search:
        '''lo = 0
        hi = x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                hi = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    lo = mid + 1
        return lo'''
