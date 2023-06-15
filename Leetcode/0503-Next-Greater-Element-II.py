class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        padding = nums * 2
        res = [-1] * len(padding)

        # for i in range(len(padding)-1):
        #     j = i+1
        #     while j < len(padding) and padding[j] <= padding[i]:
        #         j += 1
        #     if j < len(padding):
        #         res[i] = padding[j]
        # return res[:len(nums)]

        for i in reversed(range(len(padding))):
            if stack and padding[i] < stack[-1]:
                res[i] = stack[-1]
            elif stack and padding[i] >= stack[-1]:
                while stack and padding[i] >= stack[-1]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
            stack.append(padding[i])
        return [res[len(nums)]] + res[1 : len(nums)]


if __name__ == "__main__":
    # nums = [1,2,1]
    nums = [1, 2, 3, 4, 5]
    # nums = [5, 4, 3, 2, 1]
    results = Solution().nextGreaterElements(nums)
    print(results)
