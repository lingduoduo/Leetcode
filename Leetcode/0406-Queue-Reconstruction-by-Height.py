class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = {}
        for p in people:
            height, position = p[0], p[1]
            if height in d:
                d[height].append(position)
            else:
                d[height] = [position]

        res = []

        for height in sorted(d.keys(), reversed=True):
            for position in sorted(d[height]):
                res.insert(position, [height, position])
        return res


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
