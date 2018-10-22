#Use sliding window to do this question
#Check the solution, time is O(n), space is O(n)
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
        
        ans = float('inf')
        left = 0
        right = k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = i + k + 1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left = right
                right = right + k + 1
        return ans if ans != float('inf') else -1
