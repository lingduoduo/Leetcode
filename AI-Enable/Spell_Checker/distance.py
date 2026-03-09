"""Read this first."""

from typing import Dict, List, Optional, Tuple


class EditDistance:
    def compute(self, source: str, target: str, max_distance: Optional[int] = None) -> int:
        m = len(source)
        n = len(target)

        if source == target:
            return 0

        if m == 0:
            return n
        if n == 0:
            return m

        # Keep the shorter string as the DP columns to reduce memory.
        if n > m:
            source, target = target, source
            m, n = n, m

        if max_distance is not None:
            if abs(m - n) > max_distance:
                return max_distance + 1

            # Banded DP: only compute cells that can still be <= max_distance.
            big = max_distance + 1
            prev: List[int] = [big] * (n + 1)
            for j in range(min(n, max_distance) + 1):
                prev[j] = j

            for i in range(1, m + 1):
                curr: List[int] = [big] * (n + 1)
                if i <= max_distance:
                    curr[0] = i

                j_start = max(1, i - max_distance)
                j_end = min(n, i + max_distance)
                if j_start > j_end:
                    return big

                for j in range(j_start, j_end + 1):
                    cost = 0 if source[i - 1] == target[j - 1] else 1
                    curr[j] = min(
                        curr[j - 1] + 1,      # insert
                        prev[j] + 1,          # delete
                        prev[j - 1] + cost,   # substitute/match
                    )
                prev = curr
            return prev[n]

        # Standard O(m*n) time / O(n) memory DP.
        prev = list(range(n + 1))
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                cost = 0 if source[i - 1] == target[j - 1] else 1
                curr[j] = min(
                    curr[j - 1] + 1,      # insert
                    prev[j] + 1,          # delete
                    prev[j - 1] + cost,   # substitute/match
                )
            prev = curr
        return prev[n]

    def closest_words(
        self,
        word: str,
        candidates: Dict[str, int],
        max_distance: int,
    ) -> List[Tuple[str, int, int]]:
        results: List[Tuple[str, int, int]] = []
        
        for candidate, freq in candidates.items():
            # This will skip most "xword123" entries since they're much longer
            if abs(len(word) - len(candidate)) > max_distance:
                continue
                
            dist = self.compute(word, candidate, max_distance=max_distance)
            if dist <= max_distance:
                results.append((candidate, dist, freq))
        
        results.sort(key=lambda x: (x[1], -x[2]))
        return results
