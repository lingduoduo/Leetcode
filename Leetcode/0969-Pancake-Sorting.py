class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result, n = [], len(arr)
        for i in range(n, 0, -1):
            pos = arr.index(i)
            if pos == i - 1:
                continue
            if pos != 0:
                result.append(pos + 1)
                arr[: pos + 1] = arr[: pos + 1][::-1]
            result.append(i)
            arr[:i] = arr[:i][::-1]
        return result

if __name__ == '__main__':
    arr = [3,2,4,1]
    results = Solution().pancakeSort(arr)
    print(results)
