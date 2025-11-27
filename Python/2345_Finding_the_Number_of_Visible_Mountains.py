from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        n = len(peaks)

        # sort by  x-intercept(x-y) of left mountain (ascending) first,
        # and      x-intercept(x+y) of right mountain (descending)
        peaks.sort(key=lambda x: (x[0] - x[1], -(x[0] + x[1])))

        count = 0
        maxEnd = float("-inf")

        # while iterating peaks, count the number of visible peak
        # which has larger x-intercept of right mountain
        for i, (x, y) in enumerate(peaks):
            if x + y > maxEnd:
                maxEnd = x + y

                # we need to consider duplicates -> should not count
                if i < n - 1 and peaks[i] == peaks[i + 1]:
                    continue

                count += 1
        return count
