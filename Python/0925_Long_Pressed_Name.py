class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx = 0
        for i in range(len(typed)):
            if idx < len(name) and name[idx] == typed[i]:
                idx += 1
            elif i == 0 or typed[i] != typed[i - 1]:
                return False
        return idx == len(name)
