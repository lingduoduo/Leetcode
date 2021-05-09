class Solution:
    def peopleIndexes(self, favoriteCompanies):
        res = []

        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i != j and set(favoriteCompanies[i]).issubset(favoriteCompanies[j]): 
                    break
            else:
                res.append(i)
        return res
                

            # if not stack:
            #     stack.append(fav)
            #     continue
            # while stack:

            #     print(stack)
            #     for i in range(len(stack)):
            #         prev_fav = stack[i]
            #         if set(fav).isdisjoint(prev_fav):
            #             stack.append(prev_fav)
            #         elif len(fav) > len(prev_fav):
            #             stack.pop(prev_fav)
            #             stack.append(fav)


# Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
# Output: [0,1,4] 

if __name__ == '__main__':
    # favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
    favoriteCompanies = [["google"],["amazon"], ["leetcode","google","facebook"],["google","microsoft"],["google","facebook"]]
    results = Solution().peopleIndexes(favoriteCompanies)
    print(results)