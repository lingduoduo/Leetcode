class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split(" ")
        words = [word for word in words if word != ""]

        spaces = 0
        for s in text:
            if s == " ":
                spaces += 1

        if len(words) == 1:
            return words[0] + " " * spaces

        n, m = divmod(spaces, len(words) - 1)
        s_spaces = [" " * n] * (len(words) - 1)
        res = ""
        for i in range(len(words) - 1):
            res += words[i]
            res += s_spaces[i]
        res += words[-1]
        res += " " * m
        return res


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()  # split(sep=None) will discard empty strings.
        cnt = len(words)
        spaces = text.count(" ")
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
        # trailing_spaces = spaces if gap == 0 else spaces % (cnt - 1)
        trailing_spaces = spaces - gap * (cnt - 1)
        return (" " * gap).join(words) + " " * trailing_spaces


if __name__ == "__main__":
    # text = " practice   makes   perfect"
    # res = Solution().reorderSpaces(text)
    # print(res)

    text = "  hello"
    res = Solution().reorderSpaces(text)
    print(res)
