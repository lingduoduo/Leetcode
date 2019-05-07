class MyCalendarTwo(object):
    
    def __init__(self):
        self.booked = list()
        self.overlap = list()
    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        for overlap_start, overlap_end in self.overlap:
            if max(overlap_start, start) < min(overlap_end, end):
                return False
        
        for book_start, book_end in self.booked:
            ss = max(book_start, start)
            ee = min(book_end, end)
            if ss < ee:
                self.overlap.append((ss, ee))
        self.booked.append((start, end))
        return True
