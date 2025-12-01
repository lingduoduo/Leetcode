from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: x[0])
        res = 1
        cur = 1
        stack = [envelopes[0]]
        for x, y in envelopes[1:]:
            if stack[-1][1] < y:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
            stack.append([x, y])
        return res


if __name__ == "__main__":
    res = Solution().maxEnvelopes(envelopes = [[5,4],[6,4],[6,7],[2,3]])
    print(res)