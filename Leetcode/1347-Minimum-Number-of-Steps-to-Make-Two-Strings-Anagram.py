class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = collections.defaultdict(int)
        # saving the number of occurance of characters in s
        for char in s:
            d[char] += 1

        count = 0
        for char in t:
            if d[char]:
                d[char] -= 1  # if char in t is also in memo, substract that from the counted number
            else:
                count += 1
        # return count #or
        return sum(d.values())