'''Sort two array first. Use greedy algorithm to iter two arrays. 
If greedy factor is bigger than the size of cookie, iter next cookie to find the sufficient one. 
If greedy factor is equal to or smaller than the size of cookie, give this cookie and add one in output.'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                count += 1
        return count
