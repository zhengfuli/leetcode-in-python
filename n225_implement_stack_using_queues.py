import collections
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        i = len(self.queue) - 1

        while i > 0:
            self.queue.append(self.queue.popleft())
            i -= 1

        return self.queue.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()