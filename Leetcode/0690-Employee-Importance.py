class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ###First Method: DFS
        d = dict()
        for employee in employees:
            d[employee.id] = employee

        def dfs(id):
            tot = d[id].importance
            for subordinate in d[id].subordinates:
                tot += dfs(subordinate)
            return tot

        return dfs(id)


if __name__ == "__main__":
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    result = Solution().getImportance(employees, id)
    print(result)
