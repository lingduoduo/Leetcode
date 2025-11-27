class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)

        first = arr.pop(0)
        second = arr.pop(0)
        if first > second:
            winner = first
            arr.append(second)
        else:
            winner = second
            arr.append(first)
        if k == 1:
            return winner

        cnt = 1
        while arr:
            cur = arr.pop(0)
            if winner > cur:
                cnt += 1
                if cnt >= k:
                    return winner
                arr.append(cur)
            else:
                arr.append(winner)
                winner = cur
                cnt = 1


if __name__ == "__main__":
    # arr = [2,1,3,5,4,6,7]
    # k = 2
    arr = [3, 2, 1]
    k = 10
    results = Solution().getWinner(arr, k)
    print(results)
