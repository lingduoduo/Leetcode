from typing import List
import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        q = []
        heapq.heappush(q, r)
        res = 1
        for interval in intervals[1:]:
            if q is not None and q[0] <= interval[0]:
                heapq.heappop(q)
                heapq.heappush(q, interval[1])
            else:
                heapq.heappush(q, interval[1])
                res += 1
        return res

if __name__ == "__main__":

    res = Solution().canAttendMeetings(intervals=[[0,30],[5,10],[15,20]])
    print(res)

    res = Solution().canAttendMeetings(intervals=[[7,10],[2,4]])
    print(res)