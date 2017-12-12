import unittest

class ListNode(object):
    def __init__(self, x):
        self.x = x
        self.next = None

class SwapNodesInPairs(object):
    def swapNodesInPairs(self, head):
        # dummy1->head(dummy2)->head.next->...
        # dummy1->head.next->head(dummy2)->...
        # head.next->head(dummy1)->head.next.next(dummy2)...
        # ...
        # initialize
        dummy1, dummy2 = ListNode(0), head
        dummy1.next = head
        new_head = dummy1

        while dummy1.next and dummy2.next:
            # swap
            dummy1.next = dummy2.next
            dummy2.next = dummy2.next.next
            dummy1.next.next = dummy2
            # update
            dummy1 = dummy2
            dummy2 = dummy2.next

        return new_head.next

class testBench(unittest.TestCase):
    def setUp(self):
        self.tb = SwapNodesInPairs()

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
        input = [[1],
                 [1, 2],
                 [1, 2, 3, 4],
                 [1, 2, 3, 4, 5]]
        output = [[1],
                  [2, 1],
                  [2, 1, 4, 3],
                  [2, 1, 4, 3, 5]]
        for i in range(len(input)):
            t_input = self.list2ListNode(input[i])
            self.assertEqual(self.listNode2List(self.tb.swapNodesInPairs(t_input)), output[i])

    def testNullInput(self):
        self.assertIsNone(self.tb.swapNodesInPairs(self.list2ListNode([])))

if __name__ == '__main__':
    unittest.main()