from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        for i, v in enumerate(nums):
            if v != 0:
                self.d[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for k, v in self.d.items():
            if k in vec.d:
                res += v * vec.d[k]
        return res


class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: v for i, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        if len(self.d.keys()) < len(vec.d.keys()):
            for k, v in self.d.items():
                if k in vec.d:
                    res += v * vec.d[k]
        else:
            for k, v in vec.d.items():
                if k in self.d:
                    res += v * self.d[k]
        return res


# Your SparseVector object will be instantiated and called as such:
if __name__ == "__main__":
    # v1 = SparseVector(nums=[1, 0, 0, 2, 3])
    # v2 = SparseVector(nums=[0, 3, 0, 4, 0])
    # ans = v1.dotProduct(v2)
    # print(ans)

    # v1 = SparseVector(nums=[0,1,0,0,0])
    # v2 = SparseVector(nums=[0,0,0,0,2])
    # ans = v1.dotProduct(v2)
    # print(ans)

    v1 = SparseVector(nums=[0, 1, 0, 0, 2, 0, 0])
    v2 = SparseVector(nums=[1, 0, 0, 0, 3, 0, 4])
    ans = v1.dotProduct(v2)
    print(ans)
