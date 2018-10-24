class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        m = {a:b for a,b in zip(position, speed)}
        position.sort(reverse = True)
        res = n
        i = 0
        while i + 1 < n:
            j = i + 1
            while j < n and (target - position[i]) / float(m[position[i]]) * m[position[j]] + position[j] >= target:
                j += 1
                res -= 1
            i = j
        return res
