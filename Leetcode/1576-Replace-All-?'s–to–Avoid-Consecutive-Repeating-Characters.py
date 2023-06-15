class Solution:
    def modifyString(self, s: str) -> str:
        d = set("abcdefghijklmnopqrstuvwxyz")

        for cha in s:
            if cha != "?" and cha in d:
                d.remove(cha)

        res = list(s)
        d = list(d)
        for idx, cha in enumerate(res):
            j = 0
            if cha == "?":
                while j < len(d) and (
                    (idx >= 1 and d[j] == res[idx - 1])
                    or (idx <= len(s) - 2 and d[j] == res[idx + 1])
                ):
                    j += 1
                res[idx] = d[j]
        return "".join(res)


if __name__ == "__main__":
    s = "?zs"
    res = Solution().modifyString(s)
    print(res)

    s = "ubv?w"
    res = Solution().modifyString(s)
    print(res)

    s = "j?qg??b"
    res = Solution().modifyString(s)
    print(res)

    s = "??yw?ipkj?"
    res = Solution().modifyString(s)
    print(res)
