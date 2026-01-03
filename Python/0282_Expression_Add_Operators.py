from typing import List
class Solution:
    def addOperators(self, num: str, target: int):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr = [], []
        val, i = 0, 0
        val_str = ""
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord("0")
            val_str += num[i]
            # Avoid "00...".
            if str(val) != val_str:
                break
            expr.append(val_str)
            print(expr)
            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result)
            expr.pop()
            i += 1
        return result

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res: List[str] = []

        def dfs(idx: int, path: List[str], value: int, last: int) -> None:
            if idx == n:
                if value == target:
                    res.append("".join(path))
                return

            cur = 0
            for i in range(idx, n):
                if i > idx and num[idx] == "0":
                    break

                cur = cur * 10 + (ord(num[i]) - ord("0"))
                if idx == 0:
                    dfs(i + 1, path + [num[idx : i + 1]], cur, cur)
                else:
                    dfs(i + 1, path + ["+", num[idx : i + 1]], value + cur, cur)
                    dfs(i + 1, path + ["-", num[idx : i + 1]], value - cur, -cur)
                    dfs(i + 1, path + ["*", num[idx : i + 1]], value - last + last * cur, last * cur)

        dfs(0, [], 0, 0)
        return res



if __name__ == "__main__":
    num = "123"
    target = 6
    results = Solution().addOperators(num, target)
