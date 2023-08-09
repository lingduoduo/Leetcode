class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        inputs = preorder.split(",")
        stack = []
        print(inputs)

        for cha in inputs:
            print(stack)
            stack.append(cha)
            while (
                len(stack) >= 3
                and stack[-1] == "#"
                and stack[-2] == "#"
                and stack[-3] != "#"
            ):
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        print(stack)

        if stack == ["#"]:
            return True
        else:
            return False


if __name__ == "__main__":
    strs = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    strs = "9,#,92,#,#"
    # strs = "1,#"
    # strs = "9,#,#,#,1"
    # strs = "1,#,#,#,#"
    results = Solution().isValidSerialization(strs)
    print(results)
