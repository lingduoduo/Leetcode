<<<<<<< HEAD
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        pt = self
        valStr = ""
        while pt:
            valStr += "->" + str(pt.val)
            pt = pt.next
        print(valStr)

class Solution:
    def printListFromTailToHead(self, listNode):
        stack = []
        pt = listNode
        while pt:
            stack.append(pt.val)
            pt = pt.next

        dummy = ListNode(-1)
        pt = dummy
        while stack:
            pt.next = ListNode(stack.pop())
            pt = pt.next
        return dummy.next

        


if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    res = Solution().printListFromTailToHead(l1)
    res.printList()
=======
class Solution:
    def replaceSpace(self, s):
    	strs = list(s)
    	for i in range(len(s)):
    		if s[i] == " ":
    			strs.append(" ")
    			strs.append(" ")

    	p1 = len(s) - 1
    	p2 = len(strs) - 1
    	while p1 >= 0 and p2 > p1:
    		print(strs)
    		if strs[p1] != " ":
    			strs[p2] = strs[p1]
    			p1 -= 1
    			p2 -= 1
    		else:
    			strs[p2] = "0"
    			p2 -= 1
    			strs[p2] = "2"
    			p2 -= 1
    			strs[p2] = "%"
    			p2 -= 1
    	return strs

if __name__ == '__main__':
    inputs = "A B"
    res = Solution().replaceSpace(inputs)
    print(res)
>>>>>>> 55a6640b481b7ebeb08cae75e347fdb2d694f9e4
