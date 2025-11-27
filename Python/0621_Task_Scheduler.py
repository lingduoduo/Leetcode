class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        most_common = max(count.values())
        num_most = len([v for v in count.values() if v == most_common])
        return max(len(tasks), (most_common - 1) * (n + 1) + num_most)
