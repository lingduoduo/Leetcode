import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        d = collections.defaultdict(int)
        res = 0
        for cha in s:
            d[cha] += 1
            if len(d.keys()) > 2:
                while len(d.keys()) > 2:
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        d.pop(s[left])
                    left += 1
            right += 1
            res = max(res, right - left)
        return res


# from collections import defaultdict
# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
#         n = len(s)
#         if n < 3:
#             return n
#         # sliding window left and right pointers
#         left, right = 0, 0
#         # hashmap character -> its rightmost position
#         # in the sliding window
#         d = defaultdict()
#         res = 2
#         while right < n:
#             # when the slidewindow contains less than 3 characters
#             d[s[right]] = right
#             right += 1
#
#             # slidewindow contains 3 characters
#             if len(d) == 3:
#                 # delete the leftmost character
#                 del_idx = min(d.values())
#                 del d[s[del_idx]]
#                 # move left pointer of the slidewindow
#                 left = del_idx + 1
#             res = max(res, right - left)
#         return res

if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstringTwoDistinct(s="ccaabbb")
    print(res)
