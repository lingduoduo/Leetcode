class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def kmp(txt, pattern):
            curr = pattern + '#' + txt
            next_arr = [0 for _ in range(len(curr))]
            i = 1
            j = 0
            while i < len(curr):
                if curr[i] == curr[j]:
                    j += 1
                    next_arr[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = next_arr[j - 1]
                    else:
                        next_arr[i] = 0
                        i += 1
            return next_arr[-1]

        idx = kmp(s[::-1], s)
        return s[idx:][::-1] + s
