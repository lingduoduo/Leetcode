from typing import List

#
# class Solution(object):
#     def partitionLabels(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         d = dict()
#
#         for i in range(len(S)):
#             d[S[i]] = i
#
#         start = 0
#         end = 0
#
#         res = []
#         for i in range(len(S)):
#             end = max(end, d[S[i]])
#             if i == end:
#                 res.append(end - start + 1)
#                 start = end + 1
#         return res
#
#
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         d = {v: k for k, v in enumerate(S)}
#         res = []
#         loc_max = float("-inf")
#         start = 0
#         for k, v in enumerate(S):
#             loc_max = max(loc_max, d[v])
#             if k == loc_max:
#                 res.append(loc_max - start + 1)
#                 start = loc_max + 1
#         return res


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # 存储每个字符最后出现的位置
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])  # 找到当前字符出现的最远位置
            if i == end:  # 如果当前位置是最远位置，表示可以分割出一个区间
                result.append(end - start + 1)
                start = i + 1

        return result


if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    result = Solution().partitionLabels(S)
    print(result)
