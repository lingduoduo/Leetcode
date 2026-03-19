"""Tests for mutual_friends_recommender."""

import unittest

from mutual_friends_recommender import recommend_by_mutual_friends
from social_network import SocialNetwork


def _build_small_network() -> SocialNetwork:
    net = SocialNetwork()
    for a, b in [
        ("Alice", "Bob"), ("Alice", "Charlie"), ("Alice", "Diana"),
        ("Bob", "Charlie"), ("Bob", "Eve"),
        ("Charlie", "Diana"), ("Charlie", "Eve"), ("Charlie", "Frank"),
        ("Diana", "Frank"), ("Diana", "Grace"),
        ("Eve", "Frank"), ("Eve", "Heidi"),
        ("Frank", "Grace"), ("Frank", "Heidi"),
        ("Grace", "Ivan"), ("Grace", "Judy"),
        ("Heidi", "Ivan"),
        ("Ivan", "Judy"),
        ("Judy", "Karl"),
        ("Karl", "Liam"),
    ]:
        net.add_friendship(a, b)
    return net


class MutualFriendsRecommenderTest(unittest.TestCase):

    def test_orders_by_mutual_friends_then_name(self) -> None:
        net = _build_small_network()

        results = recommend_by_mutual_friends(net, "Alice")

        self.assertEqual(results, ["Eve", "Frank", "Grace"])

    def test_excludes_user_and_existing_friends(self) -> None:
        net = _build_small_network()

        results = recommend_by_mutual_friends(net, "Alice")

        self.assertNotIn("Alice", results)
        self.assertNotIn("Bob", results)
        self.assertNotIn("Charlie", results)
        self.assertNotIn("Diana", results)

    def test_respects_max_recommendations(self) -> None:
        net = _build_small_network()

        results = recommend_by_mutual_friends(net, "Eve", max_recommendations=2)

        self.assertEqual(len(results), 2)

    def test_returns_empty_when_user_has_no_friends(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")

        results = recommend_by_mutual_friends(net, "Alice")

        self.assertEqual(results, [])

    def test_returns_empty_for_non_positive_limit(self) -> None:
        net = _build_small_network()

        results = recommend_by_mutual_friends(net, "Alice", max_recommendations=0)

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
