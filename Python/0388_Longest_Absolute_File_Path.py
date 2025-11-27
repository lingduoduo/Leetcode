class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack, res = [0], 0 # initialize the stack with 0 to handle the case when there's no directory
        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]
            while len(stack) > depth + 1: # pop directories that are deeper than the current one
                stack.pop()
            if '.' in name: # if it's a file, update the answer
                res = max(res, stack[-1] + len(name))
            else: # if it's a directory, push its length to the stack
                stack.append(stack[-1] + len(name) + 1)
        return res


if __name__ == "__main__":
    # strs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # strs = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    # strs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    strs = "file1.txt\nfile2.txt\nlongfile.txt"

    # strs = "a"
    res = Solution().lengthLongestPath(strs)
    print(res)
