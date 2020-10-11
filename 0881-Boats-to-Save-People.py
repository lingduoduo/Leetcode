class Solution:
    def numRescueBoats(self, people, limit) -> int:
        people.sort()
        res = 0
        left, right = 0, len(people)-1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            res += 1
        return res

if __name__ == '__main__':
    # people = [1,2]
    # people = [3,2,2,1]
    # limit = 3
    people = [3,5,3,4]
    limit = 5
    results = Solution().numRescueBoats(people, limit)
    print(results)


        
