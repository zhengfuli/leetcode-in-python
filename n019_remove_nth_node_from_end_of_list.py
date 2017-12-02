import unittest

class ListNode(object):
    def __init__(self, x):
        self.x = x
        self.next = None

class RemoveNthNodeFromEndofList(object):
    def removeNthNodeFromEndofList(self, head, n):
        if not head:
            return None
        dummy1, dummy2, i = head, head, 0

        # considering n < 1 and n > length
        if n < 1:
            n = 1

        while dummy1.next and i < n:
            dummy1, i = dummy1.next, i+1

        while dummy1.next:
            dummy2, dummy1 = dummy2.next, dummy1.next

        if i != n:
            return head.next
        else:
            dummy2.next = dummy2.next.next
            return head

class testBench(unittest.TestCase):
    def setUp(self):
        self.tb = RemoveNthNodeFromEndofList()

    def tearDown(self):
        pass

    def list2ListNode(self, list):
        head = dummy = ListNode(0)
        for c in list:
            dummy.next = ListNode(c)
            dummy = dummy.next
        return head.next

    def listNode2List(self, listNode):
        l = []
        while listNode:
            l.append(listNode.x)
            listNode = listNode.next
        return l

    def testNormalInput(self):
        output = [[1, 2, 3, 4],
                  [1, 2, 3, 4],
                  [1, 2, 3, 5],
                  [1, 2, 4, 5],
                  [1, 3, 4, 5],
                  [2, 3, 4, 5],
                  [2, 3, 4, 5]]
        for i in range(0, 7):
            input = self.list2ListNode([1, 2, 3, 4, 5])
            self.assertEqual(self.listNode2List(self.tb.removeNthNodeFromEndofList(input, i)), output[i])

    def testNullInput(self):
        self.assertIsNone(self.tb.removeNthNodeFromEndofList(self.list2ListNode([]), 2))

    def testNullOutput(self):
        self.assertIsNone(self.tb.removeNthNodeFromEndofList(self.list2ListNode([1]), 2))

if __name__ == '__main__':
    unittest.main()


