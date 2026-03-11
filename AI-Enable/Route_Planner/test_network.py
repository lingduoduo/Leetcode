"""Tests for Network. All of this is just boilerplate to make test cases compact and understandable."""

import unittest

from network import Network


class NetworkTest(unittest.TestCase):

    def test_bidirectional_connection(self) -> None:
        net = Network()
        net.add_connection("A", "B", 5, "Red")
        neighbors_a = [c.destination for c in net.get_neighbors("A")]
        neighbors_b = [c.destination for c in net.get_neighbors("B")]
        self.assertIn("B", neighbors_a)
        self.assertIn("A", neighbors_b)

    def test_travel_time_preserved(self) -> None:
        net = Network()
        net.add_connection("A", "B", 7, "Blue")
        conn = net.get_neighbors("A")[0]
        self.assertEqual(conn.travel_time, 7)

    def test_multiple_connections(self) -> None:
        net = Network()
        net.add_connection("A", "B", 3, "Red")
        net.add_connection("A", "C", 5, "Blue")
        neighbors = [c.destination for c in net.get_neighbors("A")]
        self.assertEqual(sorted(neighbors), ["B", "C"])

    def test_one_way_neighbors(self) -> None:
        net = Network()
        net.add_connection("A", "B", 4, "Express", one_way=True)
        neighbors_b = [c.destination for c in net.get_neighbors("B")]
        expected = []
        self.assertEqual(neighbors_b, expected)

    def test_travel_cost_same_line(self) -> None:
        net = Network()
        net.add_connection("A", "B", 3, "Red")
        conn = net.get_neighbors("A")[0]
        cost = net.get_travel_cost(conn, "Red")
        expected = 3
        self.assertEqual(cost, expected)


if __name__ == "__main__":
    unittest.main()
