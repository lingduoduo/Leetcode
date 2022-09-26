class Solution:
    '''
    Input: "/a/./b/../../c/"
    Output: "/c"'
    '''

    def simplifyPath(self, path: str) -> str:
        res = []
        path_list = path.split("/")
        for p in path_list:
            if p:
                if p == '..':
                    if res:
                        res.pop()
                elif p == '.':
                    continue
                else:
                    res.append(p)
        return '/' + '/'.join(res)


class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for it in path.rstrip('/').split('/'):
            if it == '.' or it == "":
                continue
            elif it == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(it)
        return '/' + '/'.join(res)


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    result = Solution().simplifyPath(path)
    print(result)

    path = "/home/"
    result = Solution().simplifyPath(path)
    print(result)

    path = "/../"
    result = Solution().simplifyPath(path)
    print(result)

    path = "/home//foo/"
    result = Solution().simplifyPath(path)
    print(result)

    path = "/a/../../b/../c//.//"
    result = Solution().simplifyPath(path)
    print(result)

    path = "/a//b////c/d//././/.."
    result = Solution().simplifyPath(path)
    print(result)
