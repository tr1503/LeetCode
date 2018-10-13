#Memorize the last index of the sum < 0. The result should be this index + 1.
#If the sum of gas - sum of costs < 0, then return -1.
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum = 0
        total = 0
        j = -1
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                j = i
                sum = 0
        if total < 0:
            return -1
        else:
            return j + 1
