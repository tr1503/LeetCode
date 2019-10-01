class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        mid = [k for k, v in counter.items() if v % 2]
        if len(mid) > 1:
            return []
        if mid == []:
            mid = ''
        else:
            mid = mid[0]
        half = ''.join([k * (v // 2) for k, v in counter.items()])
        half = [c for c in half]
        
        def backtrack(end, temp):
            if len(temp) == end:
                curr = ''.join(temp)
                res.append(curr + mid + curr[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    temp.append(half[i])
                    backtrack(end, temp)
                    visited[i] = False
                    temp.pop()
        res = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return res
