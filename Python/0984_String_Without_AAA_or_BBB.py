class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A == B:
            return "ab" * A

        listA = ["a"] * A
        listB = ["b"] * B

        res = []

        if A < B:
            A, B = B, A
            listA, listB = listB, listA

        idxA = A
        idxB = B
        while idxA + idxB > 0:
            if idxA > 0:
                res.append(listA.pop())
                idxA -= 1
            if idxA > idxB:
                res.append(listA.pop())
                idxA -= 1
            if idxB > 0:
                res.append(listB.pop())
                idxB -= 1
        return "".join(res)


if __name__ == "__main__":
    result = Solution().strWithout3a3b(2, 6)
    print(result)
