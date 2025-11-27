from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        d = {}
        for i in range(1, len(parent)):
            if parent[i] not in d:
                d[parent[i]] = [i]
            else:
                d[parent[i]].append(i)

        self.res = 1

        def dfs(i):
            if i not in d:
                return 1
            longest = 0
            second_longest = 0
            for j in d[i]:
                length = dfs(j)
                if s[i] != s[j]:
                    if length > longest:
                        second_longest = longest
                        longest = length
                    elif length > second_longest:
                        second_longest = length
            self.res = max(self.res, longest + second_longest + 1)
            return longest + 1

        dfs(0)
        return self.res
