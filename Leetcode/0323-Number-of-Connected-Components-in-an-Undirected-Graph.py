class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dist = collections.defaultdict(list)
        for source, target in edges:
            dist[source].append(target)
            dist[target].append(source)
        count = 0
        visited = set()
        queue = collections.deque()
        for x in range(n):
            if x in visited:
                continue
            queue.append(x)
            while queue:
                source = queue.popleft()
                if source in visited:
                    continue
                visited.add(source)
                for target in dist[source]:
                    queue.append(target)
            count += 1
        return count
