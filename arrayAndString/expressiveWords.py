class Solution:
    def get(self, word, index):
        length = 1
        for i in range(index + 1, len(word)):
            if word[i] != word[index]:
                return word[index], length, i
            length += 1
        return word[index], length, len(word)
    
    def check(self, S, word):
        i = 0
        j = 0
        while i < len(S) and j < len(word):
            s, sLen, i = self.get(S,i)
            w, wLen, j = self.get(word,j)
            if s != w:
                return 0
            if sLen < wLen:
                return 0
            if sLen == 2 and wLen == 1:
                return 0
        if i == len(S) and j == len(word):
            return 1
        return 0
    
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            res += self.check(S,word)
        return res
