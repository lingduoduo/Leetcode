from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (1 + n)
        for f, t, s in bookings:
            res[f - 1] += s
            res[t] -= s
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]


if __name__ == "__main__":
    res = Solution().corpFlightBookings(
        bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5
    )
    print(res)

    res = Solution().corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2)
    print(res)
