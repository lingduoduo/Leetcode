"""Mutual-friends-based recommendation helpers."""

from typing import Dict, List

from social_network import SocialNetwork


def recommend_by_mutual_friends(
    network: SocialNetwork,
    user: str,
    max_recommendations: int = 5,
) -> List[str]:
    """
    Recommend users ranked by mutual friend count.

    Because the network model only stores user ids and current friends,
    mutual connections are the strongest available ranking signal.
    """
    if max_recommendations <= 0:
        return []

    direct_friends = network.get_friends(user)
    if not direct_friends:
        return []

    mutual_counts: Dict[str, int] = {}

    for friend in direct_friends:
        for candidate in network.get_friends(friend):
            if candidate == user or candidate in direct_friends:
                continue
            mutual_counts[candidate] = mutual_counts.get(candidate, 0) + 1

    ranked_candidates = sorted(
        mutual_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    return [
        candidate
        for candidate, _ in ranked_candidates[:max_recommendations]
    ]
