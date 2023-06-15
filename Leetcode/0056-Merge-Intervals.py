class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        [[1,3],[2,6],[8,10],[15,18]]
        """
        if not intervals:
            return False

        res = []

        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                num = res.pop()
                start = num[0]
                end = max(num[1], intervals[i][1])
                res.append([start, end])

        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if res:
                prev_start, prev_end = res[-1]
                if prev_end < cur_start:
                    res.append(intervals[i])
                else:
                    res[-1][1] = max(cur_end, prev_end)
            else:
                res.append(interval[i])
            i += 1
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res


if __name__ == "__main__":
    interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = Solution().merge(interval)
