class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

if __name__ == '__main__':
    # s = "abcd"
    # k = 2
    # res = Solution().removeDuplicates(s, k)
    # print(res)

    s = "deeedbbcccbdaa"
    k = 3
    res = Solution().removeDuplicates(s, k)
    print(res)

    s = "pbbcggttciiippooaais"
    k = 2
    res = Solution().removeDuplicates(s, k)
    print(res)