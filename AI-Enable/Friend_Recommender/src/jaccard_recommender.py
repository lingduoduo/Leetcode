"""Jaccard-similarity-based recommendation helpers."""

from typing import List

from social_network import SocialNetwork


def jaccard_similarity(network: SocialNetwork, user_a: str, user_b: str) -> float:
    """Return Jaccard similarity between two users' friend sets."""
    friends_a = network.get_friends(user_a)
    friends_b = network.get_friends(user_b)
    union = friends_a | friends_b
    if not union:
        return 0.0
    intersection = friends_a & friends_b
    return len(intersection) / len(union)


def recommend_by_jaccard(
    network: SocialNetwork,
    user: str,
    max_recommendations: int = 5,
) -> List[str]:
    """
    Recommend users ranked by Jaccard similarity of friend sets.

    Excludes the user themself and any existing direct friends.
    """
    if max_recommendations <= 0:
        return []

    direct_friends = network.get_friends(user)
    candidates = [
        candidate
        for candidate in network.get_all_users()
        if candidate != user and candidate not in direct_friends
    ]

    scored_candidates = [
        (candidate, jaccard_similarity(network, user, candidate))
        for candidate in candidates
    ]
    scored_candidates = [
        (candidate, score)
        for candidate, score in scored_candidates
        if score > 0
    ]

    ranked_candidates = sorted(
        scored_candidates,
        key=lambda item: (-item[1], item[0]),
    )
    return [
        candidate
        for candidate, _ in ranked_candidates[:max_recommendations]
    ]
