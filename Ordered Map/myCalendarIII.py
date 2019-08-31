# Use bisect package in python to solve this question
# time is O(n^2), space is O(n)
class MyCalendarThree:

    def __init__(self):
        self.pos = []
        self.delta = {}
        self.max = 0

    def book(self, start: int, end: int) -> int:
        i = bisect.bisect_left(self.pos, start)
        if start not in self.delta:
            self.delta[start] = self.delta[self.pos[i-1]] if i else 0
            self.pos[i:i] = [start]
        
        j = bisect.bisect_left(self.pos, end)
        if end not in self.delta:
            self.delta[end] = self.delta[self.pos[j-1]]
            self.pos[j:j] = [end]
        for k in range(i, j):
            self.delta[self.pos[k]] = self.delta[self.pos[k]] + 1
            self.max = max(self.max, self.delta[self.pos[k]])
        
        return self.max


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
