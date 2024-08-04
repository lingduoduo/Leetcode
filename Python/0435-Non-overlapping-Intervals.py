from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0

        s_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        res = 0
        stack = [s_intervals[0]]
        for x, y in s_intervals[1:]:
            x0, y0 = stack[-1]
            if y0 <= x:
                stack.append([x, y])
            else:
                if y < y0:
                    stack.pop()
                    stack.append([x, y])
                res += 1
        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        res = 0
        for interval in intervals[1:]:
            if r <= interval[0]:
                l, r = interval
            else:
                res += 1
                if r > interval[1]:
                    l, r = interval
        return res


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        res = 0
        stack = [intervals[0]]
        for interval in intervals[1:]:
            if stack[-1][1] <= interval[0]:
                stack.append(interval)
            else:
                stack[-1][1] = min(stack[-1][1], interval[1])
                res += 1
        return res


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1, 2], [1, 2], [1, 2]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1, 2], [2, 3]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)

    # intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
    res = Solution().eraseOverlapIntervals(intervals)
    print(res)
