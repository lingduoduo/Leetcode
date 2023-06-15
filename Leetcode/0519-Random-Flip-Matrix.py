class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.M = n_rows
        self.N = n_cols
        self.total = self.M * self.N
        self.fliped = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        pos = random.randint(0, self.total - 1)
        while pos in self.fliped:
            pos = random.randint(0, self.total - 1)
        self.fliped.add(pos)
        return [pos // self.N, pos % self.N]

    def reset(self):
        """
        :rtype: void
        """
        self.fliped.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
