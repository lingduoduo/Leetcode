class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, 1 + n))
        for i in range(1, k):
            res[i:] = res[: i - 1 : -1]
        return res


from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [1]
        interval = k
        for i in range(1, k + 1):
            res.append(res[i - 1] + interval if i % 2 == 1 else res[i - 1] - interval)
            interval -= 1
            print(res)
        for i in range(k + 1, n):
            res.append(i + 1)
        return res


if __name__ == "__main__":
    res = Solution().constructArray(n=3, k=2)
    print(res)

    res = Solution().constructArray(n=5, k=2)
    print(res)
