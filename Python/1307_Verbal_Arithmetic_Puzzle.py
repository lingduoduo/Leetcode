   class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(map(len, words)) > len(result): return False  # edge case
        
        words.append(result)
        digits = [0]*10
        mp = {}  # mapping from letter to digit
        
        def fn(i, j, val):
            """Find proper mapping for words[i][-j-1] and result[-j-1] via backtracking."""
            if j == len(result): return val == 0  # base condition
            if i == len(words): return val % 10 == 0 and fn(0, j+1, val//10)
            
            if j >= len(words[i]): return fn(i+1, j, val)
            letter = words[i][-j-1]  # Using explicit negative index calculation
            if letter in mp:
                if j and j+1 == len(words[i]) and mp[letter] == 0: return False  # backtrack (no leading 0)
                if i+1 == len(words): return fn(i+1, j, val - mp[letter])
                else: 
                    return fn(i+1, j, val + mp[letter])
            else:
                for k, x in enumerate(digits):
                    if not x and (k or j == 0 or j+1 < len(words[i])):
                        mp[letter] = k
                        digits[k] = 1
                        if i+1 == len(words) and fn(i+1, j, val-k): 
                            return True
                        if i+1 < len(words) and fn(i+1, j, val+k): 
                            return True
                        digits[k] = 0
                        mp.pop(letter)
        
        return fn(0, 0, 0)
