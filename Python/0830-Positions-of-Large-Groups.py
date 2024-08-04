from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []

        res = []
        start = 0
        end = 0
        for i in range(1, len(s)):
            if s[i] == s[start]:
                end += 1
            else:
                if end - start >= 2:
                    res.append([start, end])
                start = i
                end = i
        if s[start] == s[end] and end - start >= 2:
            res.append([start, end])
        return res


if __name__ == "__main__":
    s = "abbxxxxzzy"
    res = Solution().largeGroupPositions(s)
    print(res)

    s = "abcdddeeeeaabbbcd"
    res = Solution().largeGroupPositions(s)
    print(res)

    s = "aaa"
    res = Solution().largeGroupPositions(s)
    print(res)
