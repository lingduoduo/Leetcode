class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        pointers = [0]*len(primes)
         
        for i in range(1,n):
            local_min = float("inf")
            minIndex = 0
            for j in range(len(primes)):
                if primes[j] * ugly[pointers[j]] < local_min:
                    local_min = primes[j] * ugly[pointers[j]]
                    minIndex = j
                elif primes[j] * ugly[pointers[j]] == local_min:
                    pointers[j] += 1
            ugly.append(local_min)
            pointers[minIndex] += 1
        return ugly[-1]
