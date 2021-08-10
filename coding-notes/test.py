class Solution:
    def findContinuousSequence(self, nums, target):
        res = []
        start = 1
        end = 2
        curSum = 3
        while end < target:
            if curSum > target:
                curSum -= start
                start += 1
            elif curSum < target:
                end += 1
                curSum += end
            else:
                print(start, end)
                res.append([i for i in range(start, end+1)])
                curSum -= start
                start += 1
                end += 1
                curSum += end 
        return res

if __name__ == '__main__':
    nums = [i for i in range(101)]
    res = Solution().findContinuousSequence(nums, 100)
    print(res)
  

# # ```java
#     int start = 1, end = 2;
#     int curSum = 3;
#     while (end < sum) {
#         if (curSum > sum) {
#             curSum -= start;
#             start++;
#         } else if (curSum < sum) {
#             end++;
#             curSum += end;
#         } else {
#             ArrayList<Integer> list = new ArrayList<>();
#             for (int i = start; i <= end; i++)
#                 list.add(i);
#             ret.add(list);
#             curSum -= start;
#             start++;
#             end++;
#             curSum += end;
#         }
#     }
#     return ret;
# # ```