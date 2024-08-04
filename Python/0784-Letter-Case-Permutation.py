class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = list()

        def dfs(S, i):
            if i == len(S):
                result.append("".join(S))
                return

            S[i] = S[i].lower()
            dfs(S, i + 1)
            if not S[i].isalpha():
                return
            S[i] = S[i].upper()
            dfs(S, i + 1)

        dfs(list(S), 0)
        return result
