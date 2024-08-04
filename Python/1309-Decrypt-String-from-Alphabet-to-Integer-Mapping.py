class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "#":
                char = chr(ord("a") + int(s[i]) - 1)
                stack.append(char)
            else:
                stack.pop()
                stack.pop()
                char = chr(ord("a") + int(s[i - 2 : i]) - 1)
                stack.append(char)
        return "".join(stack)


if __name__ == "__main__":
    s = "10#11#12"
    result = Solution().freqAlphabets(s)
    print(result)
