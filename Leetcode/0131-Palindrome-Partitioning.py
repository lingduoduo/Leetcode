# class Solution(object):
#     def partition(self, s):
#         self.isPalindrome = lambda s : s == s[::-1]
#         res = []
#         self.helper(s, res, [])
#         return res

#     def helper(self, s, res, path):
#         if not s:
#             res.append(path)
#             return
#         for i in range(1, len(s) + 1): #注意起始和结束位置
#             if self.isPalindrome(s[:i]):
#                 self.helper(s[i:], res, path + [s[:i]])


# class Solution(object):
#    def _partition(self, s, index, t, result):
#        if index == len(s):
#            result.append(t.copy())
#            return

#        for i in range(index+1, len(s)+1):
#            if s[index:i] == s[index:i][::-1]:
#                t.append(s[index:i])
#                self._partition(s, i, t, result)
#                t.pop()

#    def partition(self, s):
#        """
#        :type s: str
#        :rtype: List[List[str]]
#        """
#        result = list()
#        if not s:
#            return result

#        self._partition(s, 0, list(), result)
#        return result


class Solution(object):
    def partition(self, s):
        self.res = []
        self.helper(s, [])
        return self.res

    def dfs(self, s, path):
        if len(s) == 0:
            self.res.append(path)
            return

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path + [s[:i]])
