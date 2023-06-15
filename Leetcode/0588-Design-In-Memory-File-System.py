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
