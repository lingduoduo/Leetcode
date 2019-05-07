class MapSum:
    '''
    Input: insert("apple", 3), Output: Null
    Input: sum("ap"), Output: 3
    Input: insert("app", 2), Output: Null
    Input: sum("ap"), Output: 5
    '''
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = dict()
        self.sums = dict()
    
    def insert(self, key: str, val: int) -> None:
        if key in self.vals:
            update = val - self.vals[key]
        else:
            update = val
        self.vals[key] = self.vals.get(key, 0) + update
        
        for i in range(len(key)):
            self.sums[key[:(i + 1)]] = self.sums.get(key[:(i + 1)], 0) + update
        
        print(self.vals)
        print(self.sums)
    
    def sum(self, prefix: str) -> int:
        if prefix in self.sums:
            return self.sums[prefix]
        else:
            return 0


if __name__ == '__main__':
    obj = MapSum()
    obj.insert("apple", 3)
    result = obj.sum("apple")
    print(result)
    obj.insert("app", 2)
    result = obj.sum("ap")
    print(result)
    
    obj = MapSum()
    obj.insert("a", 3)
    result = obj.sum("ap")
    print(result)
