'''Use Dynamic Programming to set dp array to represent if [0, i] is a word in wordDict.
When we get one character, we need to check each character before it. 
If we find one dp value is true and the word is in wordDict from the last to the start, 
this dp value should be true and then we break the loop. Time Complexity is O(n^2).
But it can be faster by trie.'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and str(s[j:i]) in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
