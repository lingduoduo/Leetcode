from typing import List
from collections import defaultdict

from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return float("-inf")

        inc = dec = inc2 = float("-inf")
        ans = float("-inf")

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            inc_prev, dec_prev, inc2_prev = inc, dec, inc2

            # 每轮默认断开（因为必须严格单调）
            inc = dec = inc2 = float("-inf")

            if a < b:
                # 第一段：严格上升
                inc = max(
                    a + b,
                    inc_prev + b if inc_prev != float("-inf") else float("-inf")
                )

                # 第三段：严格上升
                inc2 = max(
                    inc2_prev + b if inc2_prev != float("-inf") else float("-inf"),
                    dec_prev + b if dec_prev != float("-inf") else float("-inf")
                )

            elif a > b:
                # 第二段：严格下降
                dec = max(
                    dec_prev + b if dec_prev != float("-inf") else float("-inf"),
                    inc_prev + b if inc_prev != float("-inf") else float("-inf")
                )

            res = max(res, inc2)

        return res



if __name__ == "__main__":
    res = Solution().longestBalanced(s = "zzabccy")
    print(res)

