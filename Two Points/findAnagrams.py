# use sliding window to solve this question
# see https://www.jianshu.com/p/7db25e928806
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(p) > len(s):
            return res
        m = {}
        for c in p:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        counter = len(m)
        # two pointers, one point to tail and one to head
        start = 0
        end = 0
        while end < len(s):
            c = s[end]
            if c in m:
                m[c] -= 1
                if m[c] == 0:
                    counter -= 1
            end += 1
            
            #counter condition
            while counter == 0:
                if end - start == len(p):
                    res.append(start)
                # move sliding window
                # modify counter here
                c = s[start]
                if c in m:
                    m[c] += 1
                    if m[c] > 0:
                        counter += 1
                start += 1
        return res
