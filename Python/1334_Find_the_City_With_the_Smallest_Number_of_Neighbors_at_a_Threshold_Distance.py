
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def compute_dist(start: int) -> List[float]:
            INF = float("inf")
            dist = [INF] * n
            dist[start] = 0

            # Bellman-Ford: relax up to n-1 times
            for _ in range(n - 1):
                changed = False
                for s, e, w in edges:
                    if dist[s] != INF and dist[s] + w < dist[e]:
                        dist[e] = dist[s] + w
                        changed = True
                    if dist[e] != INF and dist[e] + w < dist[s]:
                        dist[s] = dist[e] + w
                        changed = True
                if not changed:
                    break
            return dist

        best_cnt = float("inf")
        best_city = -1

        for i in range(n):
            dist = compute_dist(i)
            # count reachable cities within threshold, excluding itself
            cnt = 0
            for j in range(n):
                if j != i and dist[j] <= distanceThreshold:
                    cnt += 1

            # tie-break: choose larger index if same count
            if cnt < best_cnt or (cnt == best_cnt and i > best_city):
                best_cnt = cnt
                best_city = i

        return best_city
