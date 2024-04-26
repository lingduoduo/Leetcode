class FileSystem(object):
    def __init__(self):
        self.root = {"dirs": {}, "files": {}}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        node, type = self.getExistedNode(path)
        if type == "dir":
            return sorted(node["dirs"].keys() + node["files"].keys())
        return [path.split("/")[-1]]

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        node = self.root
        for dir in filter(len, path.split("/")):
            if dir not in node["dirs"]:
                node["dirs"][dir] = {"dirs": {}, "files": {}}
            node = node["dirs"][dir]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        dirs = filePath.split("/")
        path, file = "/".join(dirs[:-1]), dirs[-1]
        self.mkdir(path)
        node, type = self.getExistedNode(path)
        if file not in node["files"]:
            node["files"][file] = ""
        node["files"][file] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        dirs = filePath.split("/")
        path, file = "/".join(dirs[:-1]), dirs[-1]
        node, type = self.getExistedNode(path)
        return node["files"][file]

    def getExistedNode(self, path):
        """
        :type path: str
        :rtype: str
        """
        node = self.root
        for dir in filter(len, path.split("/")):
            if dir in node["dirs"]:
                node = node["dirs"][dir]
            else:
                return node, "file"
        return node, "dir"
    

from collections import defaultdict

class TrieNode:
    def __init__(self, name):
        self.name = name
        self.is_file = False
        self.content = ""
        self.next = defaultdict(TrieNode)

class FileSystem:
    def __init__(self):
        self.head = TrieNode("")
    def ls(self, path: str) -> List[str]:
        cur = self.findPath(path)
        if cur.is_file:
            return [cur.name]
        res = [p for p in cur.next]
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        self.findPath(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.findPath(filePath)
        cur.is_file = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.findPath(filePath)
        return cur.content
        
    def findPath(self, filepath: str) -> TrieNode:
        cur = self.head
        if filepath == "/":
            return cur
        paths = filepath.split("/")[1:]
        for p in paths:
            if p not in cur.next:
                cur.next[p] = TrieNode(p)
            cur = cur.next[p]
        
        return cur


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
