from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        i2r = defaultdict(list)
        d = defaultdict(int)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                i2r[ing].append(recipes[i])
            d[recipes[i]] = len(ingredients[i])
            
        res = []
        que = deque(supplies)
        while que:
            ingredient = que.popleft()
            for nei in i2r[ingredient]:
                d[nei] -= 1
                if d[nei] == 0:
                    que.append(nei)
                    res.append(nei)
        return res

if __name__ == "__main__":
    res = Solution().findAllRecipes(recipes = ["bread","sandwich","burger"], 
                                    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
                                    supplies = ["yeast","flour","meat"]
)
    print(res)