class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.words[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = 0
        j = 0
        res = float('inf')
        while i < len(self.words[word1]) and j < len(self.words[word2]):
            res = min(res, abs(self.words[word1][i] - self.words[word2][j]))
            if self.words[word1][i] < self.words[word2][j]:
                i += 1
            else:
                j += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
