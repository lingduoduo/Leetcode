class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        ["eat", "tea", "tan", "ate", "nat", "bat"]
        """

        d = dict()

        for i in range(len(strs)):
            str_key = ''.join(sorted(strs[i]))
            d[str_key] = d.get(str_key, []) + [strs[i]]
        return [v for v in d.values()]

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
