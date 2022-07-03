class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            return "//".join([s.replace("/", "#/#") for s in strs]) + "//"


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return []
        return [seg.replace("#/#", "/") for seg in s.split("//")][:-1]
