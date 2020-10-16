class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    ###    self.result = []
    ###    self.dfs(n, n, '')
    ###    return self.result
    #
    ###def dfs(self, left, right, temp):
    ###    if left == 0 and right == 0:
    ###        self.result.append(temp)
    #
    ###    if left > 0:
    ###        self.dfs(left - 1, right, temp + '(')
    ###    if left < right:
    ###        self.dfs(left, right - 1, temp + ')')
    
        if n == 0:
            return []

        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, left, right, item, res):
        if right < left:
            return
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.helper(left - 1, right, item + "(", res)
        if right > 0:
            self.helper(left, right - 1, item + ")", res)
            