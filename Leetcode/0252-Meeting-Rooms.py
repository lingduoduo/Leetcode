from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        for interval in intervals[1:]:
            if r < interval[0]:
                return False
        return True


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])
        prev_start, prev_end = intervals[0]
        for start, end in intervals[1:]:
            if prev_end > start:
                return False
            prev_start, prev_end = start, end
        return True


if __name__ == "__main__":
    res = Solution().canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]])
    print(res)

    res = Solution().canAttendMeetings(intervals=[[7, 10], [2, 4]])
    print(res)
