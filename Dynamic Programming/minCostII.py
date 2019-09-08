# Get min cost and second min cost of each house and check with previous house's color
# if min cost has conflict uses second min cost, if not we can use min cost's color
# time is O(k * n), space is O(1)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        min1 = 0
        min2 = 0
        idx1 = -1
        for i in range(len(costs)):
            m1 = float('inf')
            m2 = m1
            id1 = -1
            for j in range(len(costs[i])):
                cost = 0
                if j == idx1:
                    cost = costs[i][j] + min2
                else:
                    cost = costs[i][j] + min1
                if cost < m1:
                    m2 = m1
                    m1 = cost
                    id1 = j
                elif cost < m2:
                    m2 = cost
            min1 = m1
            min2 = m2
            idx1 = id1
        return min1
