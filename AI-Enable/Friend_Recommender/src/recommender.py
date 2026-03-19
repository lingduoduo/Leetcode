"""Friend recommendation logic."""

import heapq
import random
from typing import Dict, List

from social_network import SocialNetwork


class Recommender:
    """Recommends friends based on mutual connections."""

    def __init__(self, network: SocialNetwork):
        self.network = network

    def recommend(self, user: str, max_recommendations: int = 5) -> List[str]:
        """
        Recommend friends for a user based on mutual connections.

        Returns up to max_recommendations users, ranked by:
        1. Number of mutual friends (descending)
        2. Alphabetical order for ties
        """
        if max_recommendations <= 0:
            return []

        direct_friends = self.network.get_friends(user)
        if not direct_friends:
            return []

        mutual_counts: Dict[str, int] = {}
        get_friends = self.network.get_friends

        # Only friends-of-friends can produce valid recommendations.
        for friend in direct_friends:
            for candidate in get_friends(friend):
                if candidate == user or candidate in direct_friends:
                    continue
                mutual_counts[candidate] = mutual_counts.get(candidate, 0) + 1

        if not mutual_counts:
            return []

        top_candidates = heapq.nsmallest(
            max_recommendations,
            mutual_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )
        return [
            candidate
            for candidate, _ in top_candidates
        ]

    def random_recommend(
        self,
        user: str,
        max_recommendations: int = 5,
        seed: int | None = None,
    ) -> List[str]:
        """
        Recommend random non-friends for a user.

        Excludes the user themself and anyone already connected to them.
        A seed can be provided for deterministic results in tests.
        """
        if max_recommendations <= 0:
            return []

        direct_friends = self.network.get_friends(user)
        candidates = [
            candidate
            for candidate in self.network.get_all_users()
            if candidate != user and candidate not in direct_friends
        ]

        if not candidates:
            return []

        rng = random.Random(seed)
        sample_size = min(max_recommendations, len(candidates))
        return rng.sample(candidates, sample_size)
