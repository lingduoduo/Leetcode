from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        res = []
        for i in range(len(stations)):
            if i >= r:
                res.append(sum(stations[(i-r) : (i+r+1)]))
            else:
                res.append(sum(stations[ :(i+r+1)]))
        print(res)


if __name__ == "__main__":
    res = Solution().maxPower(stations = [1,2,4,5,0], r = 1, k = 2)
    print(res)