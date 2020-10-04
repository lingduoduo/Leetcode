class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        ["eat", "tea", "tan", "ate", "nat", "bat"]
        """

        ###d = dict()

        ###for i in range(len(strs)):
        ###    str_key = ''.join(sorted(strs[i]))
        ###    d[str_key] = d.get(str_key, []) + [strs[i]]
        ###return [v for v in d.values()]

        res = []
        if len(strs)<1:
            return strs

        d = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in d:
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]
        return d.values()

class Solution(object):
    def groupAnagrams(self, strs):        
        res = []
        if len(strs)<1:
            return strs

        d = collections.defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            d[s_sorted].append(s)
        return d.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    print(result)
