
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b_count = 0

        for c in s:
            if c == 'b':
                b_count += 1
            else:  # c == 'a'
                res = min(res + 1, b_count)

        return res