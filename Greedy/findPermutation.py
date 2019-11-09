class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = []
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == 'I':
                size = len(res)
                for j in range(i+1, size, -1):
                    res.append(j)
        return res
