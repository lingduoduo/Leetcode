class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pos = [0] * 1001
        for trip in trips:
            pos[trip[1]] += trip[0]
            pos[trip[2]] -= trip[0]
        cur = 0
        for diff in pos:
            cur += diff
            if cur > capacity:
                return False
        return True


from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
