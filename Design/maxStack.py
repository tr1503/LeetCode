class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.max.append(x)
        if x >= self.max[-1]:
            self.max.append(x)
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        maxValue = self.max[-1]
        buffer = []
        while self.top() != maxValue:
            buffer.append(self.pop())
        self.pop()
        while len(buffer) != 0:
            self.push(buffer.pop())
        return maxValue


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
