from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                if d[5] > 0:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return False
            elif bill == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    res = Solution().lemonadeChange(bills)
    print(res)

    bills = [5, 5, 10]
    res = Solution().lemonadeChange(bills)
    print(res)

    bills = [10, 10]
    res = Solution().lemonadeChange(bills)
    print(res)

    bills = [5, 5, 10, 10, 20]
    res = Solution().lemonadeChange(bills)
    print(res)
