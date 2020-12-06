class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        for cha in set(s):
            if s.count(cha) < k:
                return max(self.longestSubstring(t, k) for t in s.split(cha))
        return len(s)


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, len(set(s)) + 1):
            times = [0] * 26
            l = r = ct = dif_ct = 0
            while r < len(s):
                ind = ord(s[r]) - ord('a')
                times[ind] += 1
                if times[ind] == 1:
                    dif_ct += 1
                if times[ind] == k:
                    ct += 1
                r += 1
                
                while l < r and dif_ct > i:
                    ind = ord(s[l]) - ord('a')
                    if times[ind] == k:
                        ct -= 1
                    if times[ind] == 1:
                        dif_ct -= 1
                    times[ind] -= 1
                    l += 1
                if dif_ct == ct == i:
                    res = max(res, r - l)
        return res