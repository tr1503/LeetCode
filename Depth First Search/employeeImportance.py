"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    # Use dfs to solve this problem
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def helper(id, m, s):
            if id in s:
                # If the employee was visited, return 0
                return 0
            s.add(id)
            res = m[id].importance
            for num in m[id].subordinates:
                # dfs each subordinates and get their importance and their subordinates' importance
                res += helper(num, m, s)
            return res
        
        s = set()
        m = {}
        # Create a graph by using hash map
        for e in employees:
            m[e.id] = e
        return helper(id, m, s)
