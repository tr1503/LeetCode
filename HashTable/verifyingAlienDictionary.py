# Use hash table to compare each word by using alien dictionary's order
# time is O(n) and space is O(n)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c : i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            pre, after = words[i], words[i + 1]
            if pre == after: 
                continue
            minLen = min(len(pre), len(after))
            for j in range(minLen):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] > d[after[j]]:
                    return False
            if len(pre) > len(after) and pre[:minLen] == after:
                return False
        return True
