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
