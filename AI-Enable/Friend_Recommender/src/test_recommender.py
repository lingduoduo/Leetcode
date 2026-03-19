"""Tests for Recommender."""

import time
import unittest

from social_network import SocialNetwork
from recommender import Recommender


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


class RecommenderTest(unittest.TestCase):

    def test_basic_recommendation_order(self) -> None:
        net = _build_small_network()
        rec = Recommender(net)
        results = rec.recommend("Alice")
        self.assertGreater(len(results), 0, "should return at least one recommendation")
        self.assertEqual(results[0], "Eve")

    def test_excludes_self_and_existing_friends(self) -> None:
        net = _build_small_network()
        rec = Recommender(net)
        results = rec.recommend("Alice")
        self.assertNotIn("Alice", results)
        self.assertNotIn("Bob", results)
        self.assertNotIn("Charlie", results)
        self.assertNotIn("Diana", results)

    def test_never_recommends_user_from_friend_of_friend_walk(self) -> None:
        net = SocialNetwork()
        net.add_friendship("Alice", "Bob")
        net.add_friendship("Alice", "Charlie")
        net.add_friendship("Bob", "Charlie")
        rec = Recommender(net)

        results = rec.recommend("Alice")

        self.assertNotIn("Alice", results)
        self.assertEqual(results, [])

    def test_limit_to_five(self) -> None:
        net = _build_small_network()
        rec = Recommender(net)
        results = rec.recommend("Alice")
        self.assertLessEqual(len(results), 5, "should return at most 5 recommendations")

    def test_random_recommend_excludes_self_and_existing_friends(self) -> None:
        net = _build_small_network()
        rec = Recommender(net)

        results = rec.random_recommend("Alice", max_recommendations=10, seed=7)

        self.assertNotIn("Alice", results)
        self.assertNotIn("Bob", results)
        self.assertNotIn("Charlie", results)
        self.assertNotIn("Diana", results)
        self.assertEqual(len(results), len(set(results)))

    def test_random_recommend_is_deterministic_with_seed(self) -> None:
        net = _build_small_network()
        rec = Recommender(net)

        first = rec.random_recommend("Alice", max_recommendations=3, seed=42)
        second = rec.random_recommend("Alice", max_recommendations=3, seed=42)

        self.assertEqual(first, second)

    def test_random_recommend_returns_empty_when_no_candidates(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        rec = Recommender(net)

        results = rec.random_recommend("Alice", seed=1)

        self.assertEqual(results, [])

    def test_no_valid_candidates(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        rec = Recommender(net)
        results = rec.recommend("Alice")
        self.assertEqual(results, [])

    def test_should_be_fast(self) -> None:
        from data import get_huge_network

        users, friendships = get_huge_network()
        net = SocialNetwork()
        for user in users:
            net.add_user(user)
        for a, b in friendships:
            net.add_friendship(a, b)

        rec = Recommender(net)
        test_users = net.get_all_users()[:200]

        start = time.time()
        for user in test_users:
            rec.recommend(user)
        elapsed = time.time() - start

        expected_max = 0.05
        self.assertLess(
            elapsed,
            expected_max,
            f"took {elapsed:.3f}s for 200 queries, need < {expected_max}s",
        )


if __name__ == "__main__":
    unittest.main()
