class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aCount = 0
        lCount = 0
        
        for c in s:
            if c == 'A':
                lCount = 0
                aCount += 1
                if aCount > 1:
                    return False
            elif c == 'L':
                lCount += 1
                if lCount == 3:
                    return False
            else:
                lCount = 0
        return True
