
from typing import List
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix = 0
        count = [0] * 1024
        count[0] = 1
        res = 0
        for c in word:
            prefix ^= 1 << ord(c) - ord('a')
            res += count[prefix]
            res += sum(count[prefix ^ 1 << i] for i in range(10))
            count[prefix] += 1

        return res

if __name__ == '__main__':
    res = Solution().wonderfulSubstrings("aabb")
    print(res)


