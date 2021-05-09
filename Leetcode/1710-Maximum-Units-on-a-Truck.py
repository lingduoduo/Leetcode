from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: -x[1])
        res = 0
        for boxnum, boxunit in boxTypes:
            if truckSize >= boxnum:
                res += boxnum * boxunit
                truckSize -= boxnum
            else:
                res += truckSize * boxunit
                break
        return res
        
if __name__ == '__main__':
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    res = Solution().maximumUnits(boxTypes, truckSize)
    print(res)