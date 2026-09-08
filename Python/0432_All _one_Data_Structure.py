class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.key_to_node = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        # New key -> count = 1
        if key not in self.key_to_node:
            if self.head.next == self.tail or self.head.next.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)

            self.head.next.keys.add(key)
            self.key_to_node[key] = self.head.next
            return

        # Existing key
        cur = self.key_to_node[key]
        new_count = cur.count + 1

        # Need a new bucket
        if cur.next == self.tail or cur.next.count != new_count:
            new_node = Node(new_count)
            self._insert_after(cur, new_node)
        else:
            new_node = cur.next

        # Move key
        cur.keys.remove(key)
        new_node.keys.add(key)
        self.key_to_node[key] = new_node

        # Remove empty bucket
        if not cur.keys:
            self._remove_node(cur)

    def dec(self, key: str) -> None:
        cur = self.key_to_node[key]

        # count 1 -> remove key completely
        if cur.count == 1:
            cur.keys.remove(key)
            del self.key_to_node[key]

        else:
            new_count = cur.count - 1

            # Need previous bucket
            if cur.prev == self.head or cur.prev.count != new_count:
                new_node = Node(new_count)
                self._insert_after(cur.prev, new_node)
            else:
                new_node = cur.prev

            cur.keys.remove(key)
            new_node.keys.add(key)
            self.key_to_node[key] = new_node

        if not cur.keys:
            self._remove_node(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
