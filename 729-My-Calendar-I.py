class MyCalendar(object):

    def __init__(self):
    	self.start_lists = list()
    	self.end_lists = list()
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if start_lists is None and end_lists is None:
        	start_lists.append(start)
        	end_lists.append(end)

        for i in range(len(start_lists)):
        	if max(start_lists[i], start) < min(end_lists[i], end):
        		return False
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
