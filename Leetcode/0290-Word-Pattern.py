class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(" ")

        if len(pattern) != len(strs):
            return False

        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != strs[i]:
                    return False
            else:
                if strs[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = strs[i]
        return True
