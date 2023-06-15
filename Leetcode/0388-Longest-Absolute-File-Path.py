class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirs = input.split("\n")

        d = []
        res = 0
        for cha in dirs:
            level = cha.count("\t")
            if not d:
                curr = cha.replace("\t", "")
            elif d[-1][1] < level:
                curr = d[-1][0] + "/" + cha.replace("\t", "")
            elif d[-1][1] >= level:
                while d and d[-1][1] >= level:
                    d.pop()
                if d:
                    curr = d[-1][0] + "/" + cha.replace("\t", "")
                else:
                    curr = cha.replace("\t", "")
            if "." in curr:
                res = max(res, len(curr))
            d.append([curr, level])

        return res


if __name__ == "__main__":
    # strs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # strs = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    # strs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    strs = "file1.txt\nfile2.txt\nlongfile.txt"

    # strs = "a"
    res = Solution().lengthLongestPath(strs)
    print(res)
