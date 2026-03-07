from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            d = defaultdict(int)
            for j in range(i, n):
                d[s[j]] += 1
                if len(set(d.values())) == 1:
                    res = max(res, j - i + 1)
        return res

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            char_count = defaultdict(int)   # 每个字符出现次数
            freq_count = defaultdict(int)   # 某个频次有多少字符

            for j in range(i, n):
                ch = s[j]
                old_freq = char_count[ch]

                # 先移除旧频次
                if old_freq > 0:
                    freq_count[old_freq] -= 1
                    if freq_count[old_freq] == 0:
                        del freq_count[old_freq]

                # 更新新频次
                new_freq = old_freq + 1
                char_count[ch] = new_freq
                freq_count[new_freq] += 1

                # 如果所有出现过的字符频次都相同
                if len(freq_count) == 1:
                    res = max(res, j - i + 1)

        return res

if __name__ == "__main__":
    res = Solution().longestBalanced(s = "zzabccy")
    print(res)