class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.curr = []

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nlist = deepcopy(self.nums)
        n = len(nlist)
        self.curr = []
        for i in range(len(nlist)):
            idx = random.randint(0, n - 1)
            n -= 1
            self.curr.append(nlist.pop(idx))
        return self.curr


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums_s = self.nums[:]
        n = len(self.nums)
        for i in range(n):
            rand = random.randrange(i, n)
            nums_s[i], nums_s[rand] = nums_s[rand], nums_s[i]
        return nums_s
