class MaxHeap(object):
    def __init__(self):
        self.count = 0
        self.heap = []

    def insert(self, new):
        self.heap.append(new)
        self.count += 1
        count = self.count

        while count > 1 and self.heap[int(count/2)-1] < self.heap[count-1]:
            self.heap[int(count/2)-1], self.heap[count-1] = self.heap[count-1], self.heap[int(count/2)-1]
            count = int(count/2)

        # print(self.heap)

    def pop(self):
        res = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.count -= 1

        count = 1
        while 2 * count <= self.count:
            print(self.heap)
            j = 2 * count

            if j + 1 <= self.count:
                if self.heap[j] > self.heap[j-1]:
                    j += 1

            if self.heap[count-1] > self.heap[j-1]:
                break

            self.heap[count-1], self.heap[j-1] = self.heap[j-1], self.heap[count-1]
            count = j

        return res

    def __len__(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

class MinHeap(object):
    def __init__(self):
        self.count = 0
        self.heap = []

    def insert(self, new):
        self.heap.append(new)
        self.count += 1
        count = self.count

        while count > 1 and self.heap[int(count/2)-1] > self.heap[count-1]:
            self.heap[int(count/2)-1], self.heap[count-1] = self.heap[count-1], self.heap[int(count/2)-1]
            count = int(count/2)

        # print(self.heap)

    def pop(self):
        res = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.count -= 1

        count = 1
        while 2 * count <= self.count:
            # print(self.heap)
            j = 2 * count

            if j + 1 <= self.count:
                if self.heap[j] < self.heap[j-1]:
                    j += 1

            if self.heap[count-1] < self.heap[j-1]:
                break

            self.heap[count-1], self.heap[j-1] = self.heap[j-1], self.heap[count-1]
            count = j

        return res

    def __len__(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap, self.max_heap = MinHeap(), MaxHeap()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.max_heap.insert(num)


    def findMedian(self):
        """
        :rtype: float
        """



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
