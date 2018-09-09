'''Use sliding window and hash table to solve. Time complexity is O(n).'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dict = {}
        ans = 0
        flag = 0
        for i in range(len(s)):
            if s[i] in dict:
                #If character repeats, move the start character to the next of last repeated character
                #We only need to check from the last repeated character + 1
                flag = max(dict[s[i]], flag)
            ans = max(ans, i - flag + 1) #Extand sliding window
            dict[s[i]] = i + 1 #Set the next index's value as this char's value in dictionary
        return ans
