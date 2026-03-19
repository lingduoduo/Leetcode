"""Read this first."""

from typing import Dict, List, Set


class SocialNetwork:
    def __init__(self) -> None:
        self._friends: Dict[str, Set[str]] = {}

    def add_user(self, name: str) -> None:
        if name not in self._friends:
            self._friends[name] = set()

    def add_friendship(self, user_a: str, user_b: str) -> None:
        self.add_user(user_a)
        self.add_user(user_b)
        self._friends[user_a].add(user_b)
        self._friends[user_b].add(user_a)

    def get_friends(self, user: str) -> Set[str]:
        return self._friends.get(user, set())

    def get_all_users(self) -> List[str]:
        return list(self._friends.keys())

    def mutual_friends_count(self, user_a: str, user_b: str) -> int:
        friends_a = self.get_friends(user_a)
        friends_b = self.get_friends(user_b)
        if len(friends_a) > len(friends_b):
            friends_a, friends_b = friends_b, friends_a
        return sum(1 for friend in friends_a if friend in friends_b)

    def is_valid_recommendation(self, user: str, candidate: str) -> bool:
        if user == candidate:
            return False
        if candidate in self.get_friends(user):
            return False
        if self.mutual_friends_count(user, candidate) < 1:
            return False
        return True
