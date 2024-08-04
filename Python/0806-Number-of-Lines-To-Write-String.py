import bisect


class Solution:
    def numberOfLines(self, widths, s: str):
        rows = 0
        cols = 0
        for cha in s:
            cols += widths[ord(cha) - ord("a")]
            if cols > 100:
                rows += 1
                cols = widths[ord(cha) - ord("a")]

        return [rows + 1, cols]


if __name__ == "__main__":
    # widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    # s = "abcdefghijklmnopqrstuvwxyz"
    # res = Solution().numberOfLines(widths, s)
    # print(res)

    widths = [
        4,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ]
    s = "bbbcccdddaaa"
    res = Solution().numberOfLines(widths, s)
    print(res)
