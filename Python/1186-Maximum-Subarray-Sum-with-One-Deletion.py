class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if not n:
            return 0

        # Initialize the keep and delete arrays
        keep = [0] * n
        delete = [0] * n

        # Base cases
        keep[0] = arr[0]
        delete[0] = float(
            "-inf"
        )  # It's not meaningful to delete the first element only

        for i in range(1, n):
            keep[i] = max(keep[i - 1] + arr[i], arr[i])
            delete[i] = max(keep[i - 1], delete[i - 1] + arr[i])

        return max(max(keep), max(delete))
