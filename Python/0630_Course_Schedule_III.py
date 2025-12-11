class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by end time (deadline)
        courses.sort(key=lambda x: x[1])

        max_heap = []  # Python only has min-heap, so store negative durations
        time = 0

        for duration, deadline in courses:
            if time + duration <= deadline:
                # take the course
                heapq.heappush(max_heap, -duration)
                time += duration
            else:
                # check if we can replace a longer course already taken
                if max_heap and -max_heap[0] > duration:
                    time += duration + heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -duration)

        return len(max_heap)
