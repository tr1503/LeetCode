class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        res.append(S)
        for i in range(len(S)):
            if S[i].isalpha():
                n = len(res)
                for j in range(n):
                    temp = list(res[j])
                    temp[i] = temp[i].swapcase()
                    res.append(''.join(temp))
        return res
