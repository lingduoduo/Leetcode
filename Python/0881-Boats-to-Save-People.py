from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            res += 1
            r -= 1
        return res


if __name__ == "__main__":
    # people = [1,2]
    # people = [3,2,2,1]
    # limit = 3
    people = [3, 5, 3, 4]
    limit = 5
    results = Solution().numRescueBoats(people, limit)
    print(results)
