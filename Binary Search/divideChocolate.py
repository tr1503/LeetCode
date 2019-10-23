class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l = 0
        r = sum(sweetness) // (K + 1)
        while l < r:
            mid = (l + r + 1) // 2
            count = curr = 0
            for s in sweetness:
                curr += s
                if curr >= mid:
                    curr = 0
                    count += 1
            if count >= K + 1:
                l = mid
            else:
                r = mid - 1
        return l
