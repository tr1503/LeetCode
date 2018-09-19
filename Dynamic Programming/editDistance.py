'''Use dynamic programming to set a 2D dp matrix. 
i and j in this dp matrix represent the number of operations for word1[0,i] and word[0,j].
There are three situations: 
a) Insert one character: dp[i][j] = dp[i-1][j] + 1,
b) Delete one character: dp[i][j] = dp[i][j-1] + 1,
c) Change one character: if two characters are different, dp[i][j] = dp[i][j] + 1, otherwise dp[i][j] = dp[i-1][j-1].
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        #For word2 is not empty, word1 is empty, it needs length of word2's operations 
        for j in range(1, len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            #For word1 is not empty, word2 is empty, it needs length of word1's operations
            dp[i][0] = i
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    dp[i][j] += 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i][j])
        
        return dp[len(word1)][len(word2)]
