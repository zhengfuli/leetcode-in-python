import unittest
from n001_two_sum import TwoSum

class TestTwoSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dut = TwoSum()

    @classmethod
    def tearDownClass(cls):
        pass

    def testOneMatch(self):
        self.assertEqual(self.dut.twoSum([2, 4, 1, 5, 8], 6), [0, 1])

    def testNoMatch(self):
        self.assertIsNone(self.dut.twoSum([], 6))
        self.assertIsNone(self.dut.twoSum([9, -1, 4, 3, 5, 6], 6))