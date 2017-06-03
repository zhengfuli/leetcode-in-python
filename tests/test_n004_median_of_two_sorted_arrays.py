import unittest
from n004_median_of_two_sorted_arrays import MedianOfTwoSortedArrays

class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.dut = MedianOfTwoSortedArrays()

    def testNullArrays(self):
        self.assertIsNone(self.dut.medianOfTwoSortedArrays([], []))
        self.assertEqual(self.dut.medianOfTwoSortedArrays([], [1]), 1.0)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([1, 2], []), 1.5)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([-1, 3, 5], []), 3.0)

    def testNormalArrays(self):
        self.assertEqual(self.dut.medianOfTwoSortedArrays([0], [0]), 0)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([-1, 1], [0]), 0)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([2.2, 4.3, 6, 8, 10, ], [0.1, 0.2, 2.1]), 3.25)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([1, 2, 3, 4], [5.01, 6, 7, 8, 9, 10]), 5.505)
        self.assertEqual(self.dut.medianOfTwoSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 8, 11, 12]), 5.5)
