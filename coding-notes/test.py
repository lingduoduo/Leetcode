class Solution:
    def permutation(self, strs: str):
        self.res = []

        chars = list(strs)
        chars.sort()

        visited = [False] * len(strs)

        self.backtracking(chars, visited, path=[])
        return self.res

    def backtracking(self, chars, visited, path):
        print(path, visited)
        if len(chars) == len(path):
            self.res.append("".join(path[:]))
            return

        for i in range(len(chars)):
            if visited[i]:
                continue
            if (i != 0 and chars[i] == chars[i-1]) and not visited[i-1]:
                continue
            visited[i] = True
            path.append(chars[i])
            self.backtracking(chars, visited, path)
            path.pop()
            visited[i] = False

if __name__ == '__main__':
    res = Solution().permutation(strs="aabc")
    print(res)

