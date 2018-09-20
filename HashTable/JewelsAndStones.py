class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        res = []
        for c in S:
            if c in J:
                res.append(c)
        return len(res)
