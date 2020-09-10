class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return []

        self.res = []
        self.dfs(s, [])
        return self.res

    # def dfs(self, s, path):
    #     if len(s)> (4-len(path))*3:
    #         return
    #     if not s and len(path)==4:
    #         self.res.append('.'.join(path))
    #         return
    #     for i in range(min(3, len(s))):
    #         curr = s[:i+1]
    #         if (curr[0]=='0' and len(curr)>=2 or int(curr)>255):
    #             continue
    #         self.dfs(s[i+1:], path+[s[:i+1]])

    def dfs(self, s, path):
        if not s and len(path) == 4:
            self.res.append('.'.join(path))
            return

        for i in range(1, 4):
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]])