# class Solution(object):
#     def generateParenthesis(self, n):
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
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if right < left:
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if right > 0:
            self.dfs(res, left, right - 1, path + ')')

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

if __name__ == '__main__':
    results = Solution().generateParenthesis(1)
    print(results)

            