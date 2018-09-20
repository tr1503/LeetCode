class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        def helper(i):
            #If the roman reaches the end, return it's integer
            if i == len(s) - 1: 
                return roman[s[i]]
            #Normal condition like LVIII
            if roman[s[i]] >= roman[s[i+1]]:
                return roman[s[i]] + helper(i+1)
            #Consider condition like IV
            else:
                return helper(i+1) - roman[s[i]]
        return helper(0)
