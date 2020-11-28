class Solution:
    def fallingSquares(self, positions):
        history = []
        res = []
        stack = []
        for i, (pos, height) in enumerate(positions):
            print(stack)
            stack.append(height)
            for j, (hisPos, hisLength) in enumerate(history):
                if (pos + height <= hisPos or hisPos + hisLength <= pos) == False:
                    stack[-1] = max(stack[-1], height+stack[j])
            if len(res) == 0:
                res.append(stack[-1])
            else:
                res.append(max(res[-1], stack[-1]))
            history.append([pos, height])
        return res

if __name__ == '__main__':
    positions = [[1, 2], [2, 3], [6, 1]]
    res = Solution().fallingSquares(positions)
    print(res)