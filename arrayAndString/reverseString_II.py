class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverse(str,0,len(str) - 1)
        start = 0
        for i in range(0, len(str)-1, 1):
            if str[i] == ' ':
                self.reverse(str, start, i-1)
                start = i + 1
        self.reverse(str, start, len(str) - 1)
        
    def reverse(self, str, start, end):
        while start < end:
            temp = str[end]
            str[end] = str[start]
            str[start] = temp
            start += 1
            end -= 1
