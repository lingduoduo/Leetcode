class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        filtered = []
        for r in restaurants:
            # apply filters
            if r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance:
                filtered.append(r)
        # sort filtered restaurants by rating (descending) and id (descending)
        filtered.sort(key=lambda r: (-r[1], -r[0]))
        # extract and return restaurant ids
        return [r[0] for r in filtered]
