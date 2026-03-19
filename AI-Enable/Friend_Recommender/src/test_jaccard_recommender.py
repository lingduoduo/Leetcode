"""Tests for jaccard_recommender."""

import unittest

from jaccard_recommender import jaccard_similarity, recommend_by_jaccard
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


class JaccardRecommenderTest(unittest.TestCase):

    def test_jaccard_similarity_basic_case(self) -> None:
        net = SocialNetwork()
        net.add_friendship("Alice", "Bob")
        net.add_friendship("Alice", "Charlie")
        net.add_friendship("Diana", "Bob")

        score = jaccard_similarity(net, "Alice", "Diana")

        self.assertAlmostEqual(score, 0.5)

    def test_jaccard_similarity_empty_union_is_zero(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        net.add_user("Bob")

        score = jaccard_similarity(net, "Alice", "Bob")

        self.assertEqual(score, 0.0)

    def test_recommend_by_jaccard_orders_results(self) -> None:
        net = _build_small_network()

        results = recommend_by_jaccard(net, "Alice")

        self.assertEqual(results, ["Eve", "Frank", "Grace"])

    def test_recommend_by_jaccard_excludes_self_and_existing_friends(self) -> None:
        net = _build_small_network()

        results = recommend_by_jaccard(net, "Alice")

        self.assertNotIn("Alice", results)
        self.assertNotIn("Bob", results)
        self.assertNotIn("Charlie", results)
        self.assertNotIn("Diana", results)

    def test_recommend_by_jaccard_returns_empty_when_no_candidates_score(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        net.add_user("Bob")

        results = recommend_by_jaccard(net, "Alice")

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
