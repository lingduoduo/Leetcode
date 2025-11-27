import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        que = collections.deque()
        que.append(("0000", 0))
        visited = set(("0000"))

        while que:
            node, steps = que.popleft()
            if node in deadends:
                continue
            if node == target:
                return steps

            for i in range(4):
                num = int(node[i])
                for d in [-1, 1]:
                    newnum = str((num + d + 10) % 10)
                    newnode = node[:i] + newnum + node[i + 1 :]
                    if newnode not in visited:
                        que.append((newnode, steps + 1))
                        visited.add(newnode)
        return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        que = collections.deque()
        que.append(("0000", 0))
        visited = set("0000")

        while que:
            node, steps = que.popleft()
            if node in deadends:
                continue
            if node == target:
                return steps

            for i in range(4):
                for j in range(10):
                    for d in [1, -1]:
                        newnode = (
                            node[:i] + str((int(node[i]) + d) % 10) + node[i + 1 :]
                        )
                        if newnode not in visited:
                            que.append((newnode, steps + 1))
                            visited.add(newnode)
        return -1
