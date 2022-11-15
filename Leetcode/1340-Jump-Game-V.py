from typing import List
import collections
import functools


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = collections.defaultdict(list)

        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        graph[j].append(i)
                stack.append(i)

        jump(range(n))
        jump(reversed(range(n)))

        @functools.lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)

        return max(map(height, range(n)))

if __name__ == "__main__":
    res = Solution().maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2)
    print(res)