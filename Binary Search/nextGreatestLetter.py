class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if target < letters[0] or target > letters[-1]:
            return letters[0]
        
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start % n]
