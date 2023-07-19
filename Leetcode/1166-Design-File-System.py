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
