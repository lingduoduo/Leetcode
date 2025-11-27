import collections

# class MapSum:
#     '''
#     Input: insert("apple", 3), Output: Null
#     Input: sum("ap"), Output: 3
#     Input: insert("app", 2), Output: Null
#     Input: sum("ap"), Output: 5
#     '''

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.vals = dict()
#         self.sums = dict()

#     def insert(self, key: str, val: int) -> None:
#         if key in self.vals:
#             update = val - self.vals[key]
#         else:
#             update = val
#         self.vals[key] = self.vals.get(key, 0) + update

#         for i in range(len(key)):
#             self.sums[key[:(i + 1)]] = self.sums.get(key[:(i + 1)], 0) + update

#         print(self.vals)
#         print(self.sums)

#     def sum(self, prefix: str) -> int:
#         if prefix in self.sums:
#             return self.sums[prefix]
#         else:
#             return 0


class Node(object):
    def __init__(self, count=0):
        self.children = collections.defaultdict(Node)
        self.count = count


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        curr = self.root
        delta = val - self.keys.get(key, 0)

        # 更新保存键值对的keys
        self.keys[key] = val
        curr = self.root
        # 更新节点的count
        curr.count += delta
        for char in key:
            curr = curr.children[char]
            curr.count += delta

        tmp = self.root
        tmp.children

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count


if __name__ == "__main__":
    obj = MapSum()
    obj.insert("apple", 3)
    result = obj.sum("apple")
    print(result)
    # obj.insert("app", 2)
    # result = obj.sum("ap")
    # print(result)

    # obj = MapSum()
    # obj.insert("a", 3)
    # result = obj.sum("ap")
    # print(result)
