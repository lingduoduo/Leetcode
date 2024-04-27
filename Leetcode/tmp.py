from typing import List
from collections import defaultdict, deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d =  defaultdict(list)
        for i, v in enumerate(s):
            if v not in d:
                d[v] = [i, i]
            else:
                d[v][1] = i
        values = sorted(d.values())
        stack = [values[0]]
        for i in range(1, len(values)):
            if values[i][0] > stack[-1][1]:
                stack.append(values[i])
            else:
                stack[-1][1] = max(stack[-1][1], values[i][1])
        res = [v[1] - v[0] + 1 for v in stack]
        return res


if __name__ == "__main__":
   res = Solution().partitionLabels("ababcbacadefegdehijhklij")
   print(res)