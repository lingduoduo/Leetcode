from typing import List
import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for path in paths:
            parts = path.split()
            for i in range(1, len(parts)):
                k, v = parts[i].split("(")
                v = v.replace(")", "")
                d[v].append(parts[0] + "/" + k)
        res = []
        for k, v in d.items():
            if len(v) > 1:
                res.append(v)
        return res


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for path in paths:
            contents = path.split(" ")
            root = contents[0]
            for strs in contents[1:]:
                file, str2 = strs.split("(")
                content = str2[:-1]
                d[content].append(("/").join([root, file]))
        res = []
        for k, v in d.items():
            if len(v) > 1:
                res.append(v)
        return res


if __name__ == "__main__":
    paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
    res = Solution().findDuplicate(paths)
    print(res)
