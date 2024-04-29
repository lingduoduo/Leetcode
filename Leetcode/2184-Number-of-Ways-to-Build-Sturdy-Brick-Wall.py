import collections

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        combos = []
        def get_combos(cur, cur_sum):                     # 1. find all possible bottom row combination (combos)
            nonlocal combos, width
            if cur_sum > width: 
                return
            if cur_sum == width:
                combos.append(tuple(cur))                 # if width matches, add to `combos`
                return
            for brick in bricks:
                get_combos(cur + [brick], cur_sum + brick)
        get_combos([], 0)
        
        d = collections.defaultdict(list)                 # make a adjacency list for {combo: [possible_neighbor_row...]}
        
        for i, combo in enumerate(combos):                # 2. for each `combo`, find its possible neighbor row
            s, cur = set(), 0
            for val in combo[:-1]:                        # use set `s` to store all join location, we don't care the right edge (hence combo[:-1]) 
                s.add(cur:=cur+val)
            for j, nei in enumerate(combos):    
                cur = 0                
                for val in nei[:-1]:
                    cur += val
                    if cur in s: break                    # if `combo` and its neighbor row `nei` join bricks at `cur`, then this neighbor can't be used at upper row
                else:                        
                    d[combo].append(nei)
                    
        ans, mod = 0, int(1e9+7)
        
        @cache
        def dfs(combo, h):                                # count number of ways build brick up to `height` \
            nonlocal ans, d, height                       #   with current row as `combo` at the `h`th row
            if height == h: return 1
            return sum(dfs(nei, h+1) for nei in d[combo])
            
        for combo in combos:                              # 3. for each `combo`, starting from bottom row, build up to `height`
            ans += dfs(combo, 1) % mod                    # count all possible ways and take the sum
            
        return ans % mod      


    class Solution:
        def buildLayouts(self, bricks, width, i, cur):
            layouts = []
            for b in bricks:
                if i + b == width:
                    layouts.append(cur)
                elif i + b < width:
                    layouts.extend(self.buildLayouts(bricks, width, i + b, cur | (1 << (i + b - 1))))
            return layouts     
        
        def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
            kMod = 1000000007
            layouts = self.buildLayouts(bricks, width, 0, 0)

            compatible = {layout: list(filter(lambda layout2: layout & layout2 == 0, layouts)) for layout in layouts}
            
            ways, ways_prev = {}, {layout: 1 for layout in layouts}
            for i in range(1, height):
                ways = {layout: sum(ways_prev[layout2] for layout2 in compatible[layout]) % kMod for layout in layouts}
                ways_prev, ways = ways, {}

            return sum(ways_prev.values()) % kMod

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        bricks.sort()
        #if the smallest brick is larger than width, there are no ways
        if bricks[0] > width:
            return 0
        
        memo = {}
        #build all possible combos for each layer, represented as a bitmask
        def build_layer(i, so_far):
            #try each brick
            for brick in bricks:
                #if the brick is too large to fit, then we break since it's sorted
                if i + brick > width:
                    break
                #if it's just right, we add as possible layer
                if i + brick == width:
                    #note we don't add the last brick, since the problem says
                    #the bricks can join at the end of the wall
                    memo[len(memo)] = so_far
                    break
                #we add a brick to the wall, 
                #so_far | 1 << i + brick 
                #will add a 1 end position where the last brick ends
                build_layer(i + brick, so_far | 1 << i + brick)
            return
        
        build_layer(0, 0)

        #now we will run a recursive function that takes what height you have so far
        #and what the previous layer looked like
        @cache
        def backtrack(h, prev_layer):
            #if you're already at the height
            if h == height:
                #this is 1 possible way to build the wall
                return 1
            ans = 0
            #for all possible ways to build a wall
            for layer in memo:
                #if there are no overlapping joins
                #if 01100 means there's a gap at pos 2, and pos 3 (bitmask are in reverse)
                #and 00010 means there is a gap at 1, this is a possible next layer
                #and if we and the two, since neither of the two has overlapping 1s
                #we'll get 0 when we & then together
                if not prev_layer & memo[layer]:
                    #increase the height, and set the current layer as the prev layer
                    ans += backtrack(h + 1, memo[layer]) % (10 ** 9 + 7)
            return ans

        return backtrack(0,0) % (10 ** 9 + 7)
