class Solution(object):
    def isStrobogrammtic(self, num) -> bool:
        d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        n = len(num)

        for i in range((n + 1) // 2):
            if num[i] not in d:
                return False
            elif num[i] != d[num[n - 1 - i]]:
                return False
        return True


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        res = []
        for s in list(num):
            if s not in d:
                return False
            res.append(d[s])
        return num[::-1] == "".join(res)


if __name__ == "__main__":
    res = Solution().isStrobogrammatic(num="69")
    print(res)
