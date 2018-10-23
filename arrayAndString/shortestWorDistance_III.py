class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev = False
        res = float('inf')
        p1 = -1
        p2 = -1
        if word1 == word2:
            for i, word in enumerate(words):
                if word == word1:
                    if not prev:
                        prev = True
                        p1 = i
                    else:
                        res = min(res, abs(i - p1))
                        p1 = i
        else:
            for i, word in enumerate(words):
                if word == word1:
                    p1 = i
                if word == word2:
                    p2 = i
                if p1 != -1 and p2 != -1:
                    res = min(res, abs(p1 - p2))
        return res
