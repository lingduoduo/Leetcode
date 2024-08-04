class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = [0] * (len(arr))
        visited[start] = 1
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if arr[node] == 0:
                    return True
                else:
                    for jump in [node - arr[node], node + arr[node]]:
                        if 0 <= jump < len(arr) and visited[jump] == 0:
                            stack.append(jump)
                            visited[jump] = 1
        return False


if __name__ == "__main__":
    # arr = [4,2,3,0,3,1,2]
    # start = 5
    # res = Solution().canReach(arr, start)
    # print(res)

    arr = [3, 0, 2, 1, 2]
    start = 2
    res = Solution().canReach(arr, start)
    print(res)
