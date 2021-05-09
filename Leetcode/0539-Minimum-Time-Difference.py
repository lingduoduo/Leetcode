from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = set()
        for t in timePoints:
            h,m = t.split(":")
            tot = int(h) * 60 + int(m)
            if tot in time:
                return 0
            time.add(tot)

        time = sorted(list(time))
        
        res = time[0] + 24*60 - time[-1]
        for i, t in enumerate(time):
            if i > 0:
                diff = t - time[i-1] 
                res = min(res, diff)
        return res

if __name__ == '__main__':
    timePoints = ["23:59","00:00"]
    res = Solution().findMinDifference(timePoints)
    print(res)

    timePoints = ["00:00","23:59","00:00"]
    res = Solution().findMinDifference(timePoints)
    print(res)

    timePoints = ["00:00","04:00","22:00"]
    res = Solution().findMinDifference(timePoints)
    print(res)

    timePoints = ["05:31","22:08","00:35"]
    res = Solution().findMinDifference(timePoints)
    print(res)
