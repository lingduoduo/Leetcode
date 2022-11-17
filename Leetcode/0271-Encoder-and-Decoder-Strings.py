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


from builtins import chr


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)

        # encode here is a workaround to fix BE CodecDriver error
        return chr(257).join(x for x in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == chr(258):
            return []
        return s.split(chr(257))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

