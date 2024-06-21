class Solution:
   def minimumBuckets(self, hamsters: str) -> int:
       hamsters = list(hamsters)
       res = 0
       for i, ch in enumerate(hamsters):
           if ch == 'H' and (i == 0 or hamsters[i-1] != '#'):
               if i+1 < len(hamsters) and hamsters[i+1] == '.':
                   hamsters[i+1] = '#'
               elif i and hamsters[i-1] == '.':
                   hamsters[i-1] = '#'
               else:
                   return -1
               res += 1
       return res
