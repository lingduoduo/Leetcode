class FileSystem:
    def __init__(self):
        self.d = {}
        self.d[""] = -1

    def createPath(self, path: str, value: int) -> bool:
        dirs = path.split("/")
        parent = "/".join(dirs[:-1])
        if path in self.d or parent not in self.d:
            return False
        self.d[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.d:
            return self.d[path]
        return -1

class FileSystem:

    def __init__(self):
        self.d = {}

    def createPath(self, path: str, value: int) -> bool:
        ch = self.d
        directories = path.split('/')[1:]

        for d in directories[:-1]:
            if d not in ch:
                return False
            ch = ch[d]

        last = directories[-1]
        if last not in ch:
            ch[last] = {}

        ch = ch[last]

        if "#" in ch:
            return False

        ch["#"] = value
        return True

    def get(self, path: str) -> int:
        ch = self.d
        for d in path.split('/')[1:]:
            if d not in ch:
                return -1
            ch = ch[d]

        return ch.get("#", -1)
    
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
