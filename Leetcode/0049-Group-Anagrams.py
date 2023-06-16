import collections
from typing import List


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        ["eat", "tea", "tan", "ate", "nat", "bat"]
        """
        if len(strs) < 1:
            return strs

        d = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in d:
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]
        return d.values()


class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        if len(strs) < 1:
            return strs

        d = collections.defaultdict(list)
        for s in strs:
            s_sorted = "".join(sorted(s))
            d[s_sorted].append(s)
        return d.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for cha in strs:
            d[tuple(sorted(cha))].append(cha)
        return d.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for cha in strs:
            key = [0] * 26
            for c in cha:
                key[ord(c) - ord("a")] += 1
            d[tuple(key)].append(cha)
        return d.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
