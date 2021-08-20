from typing import List
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         visited = [False] * len(nums)

#         stack = [0]
#         curr = 0
#         res = 0
#         n = 0

#         while stack:
#             node = stack.pop(0)
#             if not visited[node]:
#                 visited[node] = True
#                 stack.append(nums[node])
#                 curr += 1
#                 res = max(res, curr)
#             else:
#                 curr = 0

#                 while n < len(visited) and visited[n]:
#                     n += 1
#                 if n < len(visited):
#                     stack.append(n)
#                 else:
#                     break
#             print(stack)

#         return res


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            idx = i
            cnt = 0
            while nums[idx] != -1:
                cnt += 1 
                tmp = nums[idx]
                nums[idx] = -1
                idx = tmp
            res = max(res, cnt)
        return res

if __name__ == '__main__':
    nums = [5,4,0,3,1,6,2]
    res = Solution().arrayNesting(nums)
    print(res)