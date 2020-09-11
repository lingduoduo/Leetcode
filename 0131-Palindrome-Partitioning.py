class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, [])
        return self.res
    
    def dfs(self, s, temp):
        ####return condition
        if not s:
            self.res.append(temp[:])
            return
        
        ####backtracking
        for i in range(1, len(s) + 1):
            ss = s[:i]
            if ss == ss[::-1]:
                temp.append(ss)
                self.dfs(s[i:], temp)
                temp.pop()
