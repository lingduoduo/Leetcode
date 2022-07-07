from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        for interval in intervals[1:]:
            if r < interval[0]:
                return False
        return True


if __name__ == "__main__":
    res = Solution().canAttendMeetings(intervals=[[0,30],[5,10],[15,20]])
    print(res)

    res = Solution().canAttendMeetings(intervals=[[7,10],[2,4]])
    print(res)
