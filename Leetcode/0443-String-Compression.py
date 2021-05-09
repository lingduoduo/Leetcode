class Solution:
    def compress(self, chars) -> int:
        ###import collections
        #
        ###c = collections.Counter(chars)
        ###res = []
        #
        ###for k, v in c.items():
        ###    if v == 1:
        ###        res.append(k)
        ###    else:
        ###        res.append(k)
        ###        for cha in str(v):
        ###            res.append(cha)
        #
        ###return res
        
        n = len(chars)
        i, count = 0, 1
        
        for j in range(1, n-1):
            if j < n and chars[j-1] == chars[j]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for cha in str(count):
                        chars[i] = cha
                        i += 1
                count = 1
        return i
                
        
        
        
if __name__ == "__main__":
    numbers =["a","a","b","b","c","c","c"]
    numbers = ["c"]
    numbers = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    result = Solution().compress(numbers)
    print(result)