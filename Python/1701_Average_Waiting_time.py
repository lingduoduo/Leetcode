from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free = 0
        tot = 0

        for x, y in customers:
            if free < x:
                free = x
            free += y
            tot += free - x

        return tot / len(customers)

if __name__ == "__main__":
    res = Solution().averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]])
    print(res)

