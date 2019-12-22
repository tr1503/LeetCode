class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        aWord = A.split(' ')
        bWord = B.split(' ')
        aDict = {}
        bDict = {}
        for word in aWord:
            if word not in aDict:
                aDict[word] = 1
            else:
                aDict[word] += 1
        for word in bWord:
            if word not in bDict:
                bDict[word] = 1
            else:
                bDict[word] += 1
        res = []
        for word in aDict:
            if aDict[word] == 1 and word not in bDict:
                res.append(word)
        for word in bDict:
            if bDict[word] == 1 and word not in aDict:
                res.append(word)
        return res
