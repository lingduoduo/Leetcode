class Solution:
    def defangIPaddr(self, address: str) -> str:
        tmp = address.split(".")
        return "[.]".join(tmp)
