class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        maxIncEnd = [0] * n
        maxIncEnd[0] = nums[0]
        for i in range(1, n):
            maxIncEnd[i] = nums[i]
            if nums[i - 1] < nums[i] and maxIncEnd[i - 1] > 0:
                maxIncEnd[i] += maxIncEnd[i - 1]

        maxIncStart = [0] * n
        maxIncStart[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            maxIncStart[i] = nums[i]
            if nums[i] < nums[i + 1] and maxIncStart[i + 1] > 0:
                maxIncStart[i] += maxIncStart[i + 1]

        res = float("-inf")
        i = 0
        while i < n - 1:
            if nums[i] > nums[i + 1]:
                l = i
                j = i
                while j < n - 1 and nums[j] > nums[j + 1]:
                    j += 1
                r = j  # [l..r] 是最大严格递减段

                if l > 0 and r < n - 1 and l < r:
                    if nums[l - 1] < nums[l] and nums[r] < nums[r + 1]:
                        mid_sum = pre[r + 1] - pre[l]
                        cand = maxIncEnd[l - 1] + mid_sum + maxIncStart[r + 1]
                        if cand > res:
                            res = cand

                i = r  # 跳过这个递减段（因为已经处理完了）
            i += 1

        return res



class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return float("-inf")

        inc = dec = inc2 = float("-inf")
        res = float("-inf")

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
