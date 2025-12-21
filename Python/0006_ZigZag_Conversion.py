class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = [""] * min(numRows, len(s))
        i = 0
        down = False

        for ch in s:
            rows[i] += ch
            if i == 0 or i == numRows - 1:
                down = not down
            i = i + 1 if down else i - 1
        return "".join(rows)

if __name__ == "__main__":
    res = Solution().convert(s = "PAYPALISHIRING", numRows = 3)
    print(res)
