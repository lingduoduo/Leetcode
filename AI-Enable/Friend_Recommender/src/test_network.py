"""Tests for SocialNetwork."""

import unittest

from social_network import SocialNetwork


class NetworkTest(unittest.TestCase):

    def test_add_user_and_get_friends(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        net.add_user("Bob")
        net.add_friendship("Alice", "Bob")
        self.assertIn("Bob", net.get_friends("Alice"))

    def test_mutual_friends(self) -> None:
        net = SocialNetwork()
        net.add_friendship("Alice", "Bob")
        net.add_friendship("Alice", "Charlie")
        net.add_friendship("Bob", "Charlie")
        count = net.mutual_friends_count("Alice", "Bob")
        self.assertEqual(count, 1)

    def test_no_self_recommendation(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        self.assertFalse(net.is_valid_recommendation("Alice", "Alice"))

    def test_bidirectional_friendship(self) -> None:
        net = SocialNetwork()
        net.add_friendship("Alice", "Bob")
        self.assertIn("Alice", net.get_friends("Bob"))

    def test_recommendation_requires_mutual_friend(self) -> None:
        net = SocialNetwork()
        net.add_user("Alice")
        net.add_user("Bob")
        net.add_user("Charlie")
        net.add_friendship("Alice", "Bob")
        result = net.is_valid_recommendation("Alice", "Charlie")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
