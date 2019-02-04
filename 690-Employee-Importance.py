"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = dict()
        for employee in employees:
            d[employee.id] = employee
            
        def dfs(id):
            tot = d[id].importance
            for subordinate in d[id].subordinates:
                tot += dfs(subordinate)
            return tot 
        return dfs(id)

