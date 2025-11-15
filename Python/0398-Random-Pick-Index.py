class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, x in enumerate(nums):
            self.pos[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
