import unittest
from n002_add_two_numbers import ListNode, AddTwoNumbers

class TestAddTwoNUmbers(unittest.TestCase):

    def setUp(self):
        self.dut = AddTwoNumbers()

    def createList(self, values):
        head = dummy = ListNode(0)

        for val in values:
            dummy.next = ListNode(val)
            dummy = dummy.next

        return head.next

    def checkValuesByNode(self, head, results):

        for res in results:
            self.assertIsNotNone(head)
            self.assertEqual(head.val, res)
            head = head.next

        self.assertIsNone(head)

    def testNumsWithSameDigits(self):
        res = self.dut.addTwoNumbers(self.createList([1, 2, 3]), self.createList([2, 3, 4]))
        self.checkValuesByNode(res, [3, 5, 7])

        res = self.dut.addTwoNumbers(self.createList([1, 2, 3]), self.createList([9, 3, 4]))
        self.checkValuesByNode(res, [0, 6, 7])

        res = self.dut.addTwoNumbers(self.createList([1, 2, 3]), self.createList([9, 7, 6]))
        self.checkValuesByNode(res, [0, 0, 0, 1])

    def testNumsWithDiffDigits(self):
        res = self.dut.addTwoNumbers(self.createList([1, 2, 3, 4]), self.createList([1, 2, 3]))
        self.checkValuesByNode(res, [2, 4, 6, 4])

        res = self.dut.addTwoNumbers(self.createList([1, 2, 3, 4]), self.createList([2, 3, 7]))
        self.checkValuesByNode(res, [3, 5, 0, 5])

    def testNullInput(self):
        res = self.dut.addTwoNumbers(self.createList([]), self.createList([2, 3, 4]))
        self.checkValuesByNode(res, [2, 3, 4])

        res = self.dut.addTwoNumbers(self.createList([]), self.createList([]))
        self.checkValuesByNode(res, [])
