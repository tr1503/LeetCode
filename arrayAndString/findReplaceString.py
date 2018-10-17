class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = ""
        i = 0
        while i < len(S):
            if i not in indexes:
                res += S[i]
                i += 1
            else:
                index = indexes.index(i)
                source = sources[index]
                target = targets[index]
                part = S[i:i + len(source)]
                if part == source:
                    res += target
                else:
                    res += part
                i += len(source)
        return res
