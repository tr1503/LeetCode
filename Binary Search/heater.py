class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = 0
        n = len(heaters)
        heaters.sort()
        for house in houses:
            left = 0
            right = n
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else: 
                    right = mid
            if right == n:
                dist1 = float('inf')
            else:
                dist1 = heaters[right] - house
            if right == 0:
                dist2 = float('inf')
            else:
                dist2 = house - heaters[right - 1]
            res = max(res, min(dist1,dist2))
        return res
        
