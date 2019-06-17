# Use heap and its nsmallest method to solve this top K problem.
# The time is O(n*logk) and space is O(n). 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = []
        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            dis.append((d,p))
        heapq.heapify(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]
