#Use dfs and hashmap to finish this question.
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        similars = collections.defaultdict(set)
        for w1, w2 in pairs:
            similars[w1].add(w2)
            similars[w2].add(w1)
        
        def dfs(word1, word2, visited):
            for similar in similars[word2]:
                if word1 == similar:
                    return True
                elif similar not in visited:
                    visited.add(similar)
                    if dfs(word1, similar, visited):
                        return True
            return False
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and not dfs(w1,w2,set([w2])):
                return False
        return True
