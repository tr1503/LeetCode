# Use greedy algorithm to get the idle slots and get the result
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        max_count = count[25] - 1
        idle = max_count * n
        i = 24
        while i >= 0 and count[i] > 0:
            idle -= min(count[i], max_count)
            i -= 1
        if idle > 0:
            return idle + len(tasks)
        else:
            return len(tasks)
