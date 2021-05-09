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