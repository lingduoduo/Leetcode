import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        que = []
        heapq.heappush(que, intervals[0][1])
        res = 1
        for i in range(1, len(intervals)):
            while que and intervals[i][0] >= que[0]:
                heapq.heappop(que)
            heapq.heappush(que, intervals[i][1])
            res = max(res, len(que))
        return res
    
# Test the code        
if __name__ == '__main__':
    res = Solution().minMeetingRooms([[0,30],[5,10],[9,15],[15,18],[16,18],[19,20],[40,41]])
    print(res)
