class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        left = 0
        right = max(bloomDay) + 1

        while left < right:
            mid = left + (right - left)// 2

            num = 0
            count = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    num += 1
                    count = 0


            if num >= m:
                right = mid
            else:
                left = mid + 1

        return left