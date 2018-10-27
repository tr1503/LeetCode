class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0 for _ in range(length + 1)]
        for update in updates:
            res[update[0]] += update[2]
            res[update[1] + 1] -= update[2]
        for i in range(1,len(res)):
            res[i] += res[i-1]
        res.pop()
        return res
