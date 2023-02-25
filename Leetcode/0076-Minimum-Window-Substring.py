class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        d = dict()
        for i in range(len(t)):
            d[t[i]] = d.get(t[i], 0) + 1

        slow = 0
        minLen = float('inf')
        matchCount = 0
        index = 0

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] -= 1
                ####from 1 to 0
                if d[s[i]] == 0:
                    matchCount += 1

            while matchCount == len(d.keys()):
                ####find a valid substring
                if i - slow + 1 < minLen:
                    minLen = i - slow + 1
                    index = slow
                leftmost = s[slow]
                slow += 1
                if leftmost not in d:
                    continue
                else:
                    ####from 0 to 1
                    d[leftmost] += 1
                    if d[leftmost] > 0:
                        matchCount -= 1

        return "" if minLen == float('inf') else s[index: index + minLen]

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        count = collections.Counter(t)
        for i, c in enumerate(s):
            print(f"left = {left}, cnt={cnt}, minLen={minLen}, count={count}")
            count[c] -= 1
            if count[c] >= 0:
                cnt += 1
            while cnt == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        left, right, minLen = 0, 0, float('inf')
        d = collections.Counter(t)
        for i, v in enumerate(s):
            d[v] -= 1
            if d[v] >= 0:
                right += 1
            while right == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                d[s[left]] += 1
                if d[s[left]] > 0:
                    right -= 1
                left += 1
        return res


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    result = Solution().minWindow(S, T)
    print(result)
