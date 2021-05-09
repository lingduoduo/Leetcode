class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        for i in range(len(ages)-1):
            for j in range(i+1, len(ages)):
                if ages[i] == ages[j]:
                    res += 2
                elif not((age[j] <= 0.5 * age[i] + 7) or (age[j] > 100 and age[i] < 100)):
                    res += 1
        return res
    
    
