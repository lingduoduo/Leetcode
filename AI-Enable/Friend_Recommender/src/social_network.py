"""Read this first."""

from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass(slots=True)
class User:
    name: str
    friends: Set[str] = field(default_factory=set)


class SocialNetwork:
    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    def add_user(self, name: str) -> None:
        if name not in self._users:
            self._users[name] = User(name=name)

    def add_friendship(self, user_a: str, user_b: str) -> None:
        self.add_user(user_a)
        self.add_user(user_b)
        self._users[user_a].friends.add(user_b)
        self._users[user_b].friends.add(user_a)

    def get_friends(self, user: str) -> Set[str]:
        user_record = self._users.get(user)
        if user_record is None:
            return set()
        return user_record.friends

    def get_all_users(self) -> List[str]:
        return list(self._users.keys())

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
