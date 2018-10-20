class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        m = {}
        for w1, w2 in pairs:
            if w1 not in m:
                m[w1] = set()
            if w2 not in m:
                m[w2] = set()
            m[w1].add(w2)
            m[w2].add(w1)
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w1 not in m:
                return False
            if w2 not in m[w1]:
                return False
        return True
