from  collections import Counter
from collections import Counter

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # Find - Get ending point of subsequence starting after s1[s]
        def find_subseq(s):
            t = 0
            while s < len(s1):
                if s1[s] == s2[t]:
                    t += 1
                    if t == len(s2):
                        break
                s += 1
            return s if t == len(s2) else None

        # Improve - Get best starting point of subsequence ending at s1[s]
        def improve_subseq(s):
            t = len(s2) - 1
            while t >= 0:
                if s1[s] == s2[t]:
                    t -= 1
                s -= 1
            return s + 1

        s, min_len, res = 0, float('inf'), ''
        while s < len(s1):
            end = find_subseq(s)  # Find end-point of subsequence
            if not end:
                break
            start = improve_subseq(end)  # Improve start-point of subsequence
            if end - start + 1 < min_len:  # Track min length
                min_len = end - start + 1
                res = s1[start:end + 1]
            s = start + 1  # Start next subsequence search

        # Handle the case when s2 has only one character separately
        if len(s2) == 1:
            for i in range(len(s1)):
                if s1[i] == s2:
                    return s2

        return res

if __name__ == "__main__":
    res = Solution().minWindow(s1 =
"ngpkbrofkbkoacqjqjmfohikc",
s2 =
"n")
    print(res)  # Output should be "bcde"


