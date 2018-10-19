class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        guess = num / 2.0
        for i in range(20):
            guess = (guess + num / guess) / 2.0
        return int(guess) == guess
