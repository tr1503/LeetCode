class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        #Set an array shows all seats have people
        people = (i for i, seat in enumerate(seats) if seat)
        prev = None
        future = next(people) 
        
        res = 0
        for i in range(len(seats)):
            if seats[i]:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people,None)
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                res = max(res,min(left,right))
        return res
