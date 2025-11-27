from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        pre = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])

        res = pre
        for i in range(len(customers)):
            if i - X >= 0 and grumpy[i - X] == 1:
                pre -= customers[i - X]
            if grumpy[i] == 1:
                pre += customers[i]
            res = max(res, pre)

        return res


if __name__ == "__main__":
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    res = Solution().maxSatisfied(customers, grumpy, X)
    print(res)

    # customers = [5,8]
    # grumpy = [0,1]
    # X = 1
    # res = Solution().maxSatisfied(customers, grumpy, X)
    # print(res)
