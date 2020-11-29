from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key=key
        self.val=val
        self.count=count
        
class LFUCache:        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.f = {}
        self.minV = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.d:  
            return -1 

        node = self.d[key]
        del self.f[node.count][key]

        if not self.f[node.count]:
            del self.f[node.count] 
            
        node.count += 1
        if not node.count in self.f:
            self.f[node.count] = OrderedDict()
        self.f[node.count][key] = node
        
        if not self.minV in self.f:
            self.minV += 1
        return node.val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #如果存在该如何处理 更新value且计数+1 
        if self.capacity == 0: 
            return None

        if key in self.d:
            self.d[key].val = value
            self.get(key)
        else:
            if len(self.d) == self.capacity:
                item = self.f[self.minV].popitem(last=False)
                del self.d[item[0]]

            node = Node(key,value,1)
            self.d[key]=node

            if not 1 in self.f:
                self.f[1] = OrderedDict()
            
            self.f[1][key] = node
            self.minV=1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
        lfu = LFUCache(2);
        lfu.put(1, 1);
        lfu.put(2, 2);
        lfu.get(1);      # return 1
        lfu.put(3, 3);   # evicts key 2
        lfu.get(2);      # return -1 (not found)
        lfu.get(3);      # return 3
        lfu.put(4, 4);   # evicts key 1.
        lfu.get(1);      # return -1 (not found)
        lfu.get(3);      # return 3
        lfu.get(4);      # return 4    
