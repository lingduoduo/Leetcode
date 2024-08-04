class Allocator:
    class Block:
        def __init__(self, size: int, free: bool = False):
            self.size = size
            self.free = free
            self.next = None

    def __init__(self, n: int):
        #self.memo = [0] * n
        self.available = n
        self.allocated = dict()
        self.head = self.Block(0, 0)
        self.head.next = self.Block(self.available, True)

    def allocate(self, size: int, mID: int) -> int:
        offset = 0
        if size <= self.available:
            prev = self.head
            p = prev.next
            while p and (not p.free or p.size < size):
                offset += p.size
                p = p.next
            if not p:
                return -1
            if size < p.size:
                sub = self.Block(p.size - size, True)
                sub.next = p.next
                p.next = sub
            p.free = False
            p.size = size
            blocks = self.allocated.setdefault(mID, set())
            blocks.add(p)
            self.available -= size
            return offset
        else:
            return -1

    def free(self, mID: int) -> int:
        r = 0
        blocks = self.allocated.get(mID)
        if blocks:
            for block in blocks:
                self.available += block.size
                r += block.size
                self.free_block(block)
            blocks.clear()
            del self.allocated[mID]
        return r

    def free_block(self, block: Block):
        block.free = True
        # merge with next block
        if block.next and block.next.free:
            block.size += block.next.size
            block.next = block.next.next

        # check if we need to merge with prev block
        prev = self.head
        p = prev.next
        while p and p != block:
            prev = p
            p = p.next
        if prev.free:
            prev.size += block.size
            prev.next = block.next