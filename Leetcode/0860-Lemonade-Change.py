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

        five = 0
        ten = 0
        twenty = 0

        for bill in bills:
            # 情况一：收到5美元
            if bill == 5:
                five += 1

            # 情况二：收到10美元
            if bill == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1

            # 情况三：收到20美元
            if bill == 20:
                # 先尝试使用10美元和5美元找零
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1
                # 如果无法使用10美元找零，则尝试使用三张5美元找零
                elif five >= 3:
                    five -= 3
                    # twenty += 1
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
