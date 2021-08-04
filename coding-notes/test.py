class Solution:

    def IsPopOrder(self, pushSequence, popSequence):
        stack = []
        for i in range(len(pushSequence)):
            stack.append(pushSequence[i])
            while stack and popSequence and stack[-1] == popSequence[0]:
                print(stack)
                popSequence.pop(0)
                stack.pop()
        return len(stack) == 0
                


if __name__ == '__main__':
    res = Solution().IsPopOrder(pushSequence=[1,2,3,4,5], popSequence=[4,5,3,2,1])
    print(res)

    res = Solution().IsPopOrder(pushSequence=[1,2,3,4,5], popSequence=[4,3,5,1,2])
    print(res)


        
# public boolean IsPopOrder(int[] pushSequence, int[] popSequence) {
#     int n = pushSequence.length;
#     Stack<Integer> stack = new Stack<>();
#     for (int pushIndex = 0, popIndex = 0; pushIndex < n; pushIndex++) {
#         stack.push(pushSequence[pushIndex]);
#         while (popIndex < n && !stack.isEmpty() 
#                 && stack.peek() == popSequence[popIndex]) {
#             stack.pop();
#             popIndex++;
#         }
#     }
#     return stack.isEmpty();
# }
