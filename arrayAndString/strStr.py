#Use KMP Algorithm to finish this question
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        #build next array
        i = 0
        j = 1
        t = [0] * len(needle)
        while j < len(needle):
            if needle[j] == needle[i]:
                t[j] = i + 1
                i += 1
                j += 1
            elif i:
                i = t[i-1]
            else:
                t[j] = 0
                j += 1
                
        #Do KMP algorithm
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j:
                j = t[j-1]
            else:
                i += 1
        if j == len(needle):
            return i - j
        else:
            return -1
