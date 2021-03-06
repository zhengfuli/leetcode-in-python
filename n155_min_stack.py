class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_stack or (self.min_stack and self.min_stack[-1] >= x): self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min_stack and self.top() == self.min_stack[-1]: self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]


            # Your MinStack object will be instantiated and called as such:
            # obj = MinStack()
            # obj.push(x)
            # obj.pop()
            # param_3 = obj.top()
            # param_4 = obj.getMin()