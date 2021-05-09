# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:

#         inputs = preorder.split(",")

#         stack = []

#         cnt = 0
#         while inputs:
#             print(inputs)
#             print(stack)
#             print(cnt)
#             ch = inputs.pop(0)
#             if ch in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
#                 stack.append(ch)
#             elif cnt==0:
#                 stack.append(ch)
#                 cnt += 1
#             else:
#                 stack.pop()
#                 stack.pop()
#                 stack.append("#")
#                 cnt = 0

#         if stack == ["#"]:
#             return True
#         else:
#             return False

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        # stack = []
        # for node in preorder.split(','):
        #     stack.append(node)
        #     while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
        #         stack.pop(), stack.pop(), stack.pop()
        #         stack.append('#')
        # return len(stack) == 1 and stack.pop() == '#' 
        

        inputs = preorder.split(",")
        stack = []
        print(inputs)

        for cha in inputs:
            print(stack)
            stack.append(cha)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3]!= "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        print(stack)


        if stack == ["#"]:
            return True
        else:
            return False           

if __name__ == '__main__':
    strs = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    strs = "9,#,92,#,#"
    # strs = "1,#"
    # strs = "9,#,#,#,1"
    # strs = "1,#,#,#,#"
    results = Solution().isValidSerialization(strs)
    print(results)