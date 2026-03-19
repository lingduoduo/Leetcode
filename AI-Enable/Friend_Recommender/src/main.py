"""
Runs the Recommender. It's useful to see how the system is called.
"""

from data import get_small_network
from social_network import SocialNetwork
from recommender import Recommender


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    users, friendships = get_small_network()
    network = SocialNetwork()
    for user in users:
        network.add_user(user)
    for a, b in friendships:
        network.add_friendship(a, b)

    recommender = Recommender(network)

    for user in ["Alice", "Eve", "Karl"]:
        recs = recommender.recommend(user)
        print(f"  {user}: {recs}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
