from typing import List

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {ch: i for i, ch in enumerate(order)}
        n = len(order)
        return "".join(sorted(s, key=lambda ch: rank.get(ch, n)))



if __name__ == "__main__":
    res = Solution().customSortString(order = "cba", s = "abcd")
    print(res)
