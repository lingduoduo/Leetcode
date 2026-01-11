from bisect import bisect_right

class SnapshotArray:
    def __init__(self, length: int):
        self.dif = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.dif[index] = val

    def snap(self) -> int:
        self.snaps.append(self.dif.copy())
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0

class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshots = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        h = self.snapshots[index]
        if h[-1][0] == self.snap_id:
            h[-1] = (self.snap_id, val)
        else:
            h.append((self.snap_id, val))

    def snap(self) -> int:
        sid = self.snap_id
        self.snap_id += 1
        return sid

    def get(self, index: int, snap_id: int) -> int:
        h = self.snapshots[index]
        i = bisect_right(h, (snap_id, 10**18)) - 1
        return h[i][1]
    
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
