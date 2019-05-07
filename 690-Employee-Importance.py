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
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11

"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # First Method: DFS
        d = dict()
        for employee in employees:
            d[employee.id] = employee
        
        def dfs(id):
            tot = d[id].importance
            for subordinate in d[id].subordinates:
                tot += dfs(subordinate)
            return tot
        
        return dfs(id)
        
        ## Second Method
        d = dict()
        sub = dict()
        
        for i, importance, subordinate in employees:
            d[i] = importance
            sub[i] = subordinate
        
        visited = []
        visited.append(id)
        res = 0
        while visited:
            node = visited.pop(0)
            res += d[node]
            
            for subordinate in sub[node]:
                visited.append(subordinate)
        return res


if __name__ == '__main__':
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    result = Solution().getImportance(employees, id)
    print(result)
